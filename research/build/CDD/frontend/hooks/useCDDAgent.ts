"use client";

/**
 * Custom hook for managing CDD agent state and SSE streaming.
 *
 * This hook handles:
 * - SSE connection to backend
 * - State updates from AG-UI events
 * - Checkpoint flow management
 */

import { useState, useCallback, useRef, useEffect } from "react";
import type { CDDAgentState, AGUIEvent, StreamingMessage, CurrentToolCall, GeneratedFile, PreviousAnalysis } from "@/lib/types";

// Direct backend URL - Next.js rewrites buffer SSE responses
const BACKEND_URL = process.env.NEXT_PUBLIC_BACKEND_URL || "http://localhost:8000";

interface UseCDDAgentReturn {
  state: CDDAgentState | null;
  isRunning: boolean;
  isComplete: boolean;
  hasError: boolean;
  isViewingPrevious: boolean;
  pendingCheckpoint: CDDAgentState["current_checkpoint"];
  currentPhase: CDDAgentState["phases"][0] | undefined;
  streamingMessages: StreamingMessage[];
  currentToolCall: CurrentToolCall | null;
  generatedFiles: GeneratedFile[];
  start: (companyName: string) => Promise<void>;
  stop: () => void;
  loadAnalysis: (companyName: string) => Promise<void>;
  fetchAnalyses: () => Promise<PreviousAnalysis[]>;
  clearState: () => void;
  approveCheckpoint: (checkpointId: string, feedback?: string) => Promise<void>;
  rejectCheckpoint: (checkpointId: string, feedback?: string) => Promise<void>;
}

export function useCDDAgent(): UseCDDAgentReturn {
  const [state, setState] = useState<CDDAgentState | null>(null);
  const [isRunning, setIsRunning] = useState(false);
  const [isViewingPrevious, setIsViewingPrevious] = useState(false);
  const eventSourceRef = useRef<EventSource | null>(null);
  const sessionIdRef = useRef<string | null>(null);

  // Derived state
  const isComplete = state?.final_report_ready ?? false;
  const hasError = (state?.errors?.length ?? 0) > 0;
  const pendingCheckpoint = state?.current_checkpoint ?? null;
  const currentPhase = state?.phases?.find(
    (p) => p.phase_number === state?.current_phase
  );
  const streamingMessages = state?.streaming_messages ?? [];
  const currentToolCall = state?.current_tool_call ?? null;
  const generatedFiles = state?.generated_files ?? [];

  // Process incoming AG-UI events
  const processEvent = useCallback((event: AGUIEvent) => {
    switch (event.type) {
      case "STATE_SNAPSHOT":
        setState(event.data as unknown as CDDAgentState);
        break;

      case "STATE_DELTA":
        setState((prev) => {
          if (!prev) return prev;
          const { path, value } = event.data as { path: string; value: unknown };
          return { ...prev, [path]: value };
        });
        break;

      case "RUN_STARTED":
        setIsRunning(true);
        break;

      case "RUN_FINISHED":
        setIsRunning(false);
        break;

      case "RUN_ERROR":
        setIsRunning(false);
        setState((prev) => {
          if (!prev) return prev;
          return {
            ...prev,
            errors: [...prev.errors, event.data.error as string],
          };
        });
        break;

      case "CHECKPOINT_PENDING":
        setState((prev) => {
          if (!prev) return prev;
          return {
            ...prev,
            current_checkpoint: event.data as unknown as CDDAgentState["current_checkpoint"],
          };
        });
        break;

      case "TEXT_MESSAGE_CONTENT":
        // Streaming messages are now included via STATE_DELTA
        // This event can be used for additional processing if needed
        break;

      case "TOOL_CALL_START":
        setState((prev) => {
          if (!prev) return prev;
          const toolData = event.data as { tool_id: string; tool_name: string; arguments: Record<string, unknown> };
          return {
            ...prev,
            current_tool_call: {
              tool_id: toolData.tool_id,
              tool_name: toolData.tool_name,
              agent: (toolData.arguments?.agent as string) || toolData.tool_name,
              started_at: new Date().toISOString(),
            } as CurrentToolCall,
          };
        });
        break;

      case "TOOL_CALL_END":
        setState((prev) => {
          if (!prev) return prev;
          return {
            ...prev,
            current_tool_call: null,
          };
        });
        break;

      case "FILE_CREATED":
        setState((prev) => {
          if (!prev) return prev;
          const fileData = event.data as GeneratedFile;
          return {
            ...prev,
            generated_files: [...(prev.generated_files || []), {
              id: fileData.id || String(Date.now()),
              file_path: fileData.file_path,
              filename: fileData.filename,
              file_type: fileData.file_type,
              size: fileData.size,
              preview: fileData.preview,
              created_at: new Date().toISOString(),
              agent: fileData.agent,
            }],
          };
        });
        break;

      default:
        // Handle other event types as needed
        break;
    }
  }, []);

  // Start analysis
  const start = useCallback(async (companyName: string) => {
    // Close existing connection
    if (eventSourceRef.current) {
      eventSourceRef.current.close();
    }

    setIsRunning(true);
    setIsViewingPrevious(false);
    setState(null);

    try {
      // Start analysis via POST, then connect to SSE stream
      const response = await fetch(`${BACKEND_URL}/api/cdd/analyze`, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ company_name: companyName }),
      });

      if (!response.ok) {
        throw new Error(`Failed to start analysis: ${response.statusText}`);
      }

      // Get session ID from header
      sessionIdRef.current = response.headers.get("X-Session-ID");

      // Read SSE stream
      const reader = response.body?.getReader();
      const decoder = new TextDecoder();

      if (!reader) {
        throw new Error("No response body");
      }

      while (true) {
        const { done, value } = await reader.read();
        if (done) break;

        const text = decoder.decode(value);
        const lines = text.split("\n");

        for (const line of lines) {
          if (line.startsWith("data: ")) {
            try {
              const event = JSON.parse(line.slice(6)) as AGUIEvent;
              processEvent(event);
            } catch {
              // Ignore parse errors for malformed events
            }
          }
        }
      }
    } catch (error) {
      setIsRunning(false);
      setState((prev) => ({
        ...(prev ?? ({} as CDDAgentState)),
        errors: [...(prev?.errors ?? []), String(error)],
      }));
    }
  }, [processEvent]);

  // Stop analysis
  const stop = useCallback(() => {
    if (eventSourceRef.current) {
      eventSourceRef.current.close();
      eventSourceRef.current = null;
    }
    setIsRunning(false);
  }, []);

  // Approve checkpoint
  const approveCheckpoint = useCallback(
    async (checkpointId: string, feedback?: string) => {
      if (!sessionIdRef.current) return;

      try {
        const response = await fetch(
          `${BACKEND_URL}/api/cdd/sessions/${sessionIdRef.current}/checkpoint`,
          {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({
              checkpoint_id: checkpointId,
              approved: true,
              feedback,
            }),
          }
        );

        if (!response.ok) {
          throw new Error(`Failed to approve checkpoint: ${response.statusText}`);
        }

        // Read continued SSE stream
        const reader = response.body?.getReader();
        const decoder = new TextDecoder();

        if (!reader) return;

        while (true) {
          const { done, value } = await reader.read();
          if (done) break;

          const text = decoder.decode(value);
          const lines = text.split("\n");

          for (const line of lines) {
            if (line.startsWith("data: ")) {
              try {
                const event = JSON.parse(line.slice(6)) as AGUIEvent;
                processEvent(event);
              } catch {
                // Ignore parse errors
              }
            }
          }
        }
      } catch (error) {
        setState((prev) => ({
          ...(prev ?? ({} as CDDAgentState)),
          errors: [...(prev?.errors ?? []), String(error)],
        }));
      }
    },
    [processEvent]
  );

  // Reject checkpoint
  const rejectCheckpoint = useCallback(
    async (checkpointId: string, feedback?: string) => {
      if (!sessionIdRef.current) return;

      try {
        await fetch(`${BACKEND_URL}/api/cdd/sessions/${sessionIdRef.current}/checkpoint`, {
          method: "POST",
          headers: { "Content-Type": "application/json" },
          body: JSON.stringify({
            checkpoint_id: checkpointId,
            approved: false,
            feedback,
          }),
        });

        setIsRunning(false);
      } catch (error) {
        setState((prev) => ({
          ...(prev ?? ({} as CDDAgentState)),
          errors: [...(prev?.errors ?? []), String(error)],
        }));
      }
    },
    []
  );

  // Fetch list of previous analyses
  const fetchAnalyses = useCallback(async (): Promise<PreviousAnalysis[]> => {
    try {
      const response = await fetch(`${BACKEND_URL}/api/cdd/analyses`);
      if (!response.ok) {
        throw new Error(`Failed to fetch analyses: ${response.statusText}`);
      }
      const data = await response.json();
      return data.analyses as PreviousAnalysis[];
    } catch (error) {
      console.error("Failed to fetch analyses:", error);
      return [];
    }
  }, []);

  // Load a previous analysis (read-only mode)
  const loadAnalysis = useCallback(async (companyName: string) => {
    try {
      const response = await fetch(`${BACKEND_URL}/api/cdd/analyses/${encodeURIComponent(companyName)}`);
      if (!response.ok) {
        throw new Error(`Failed to load analysis: ${response.statusText}`);
      }
      const data = await response.json();
      setState(data as CDDAgentState);
      setIsViewingPrevious(true);
      setIsRunning(false);
    } catch (error) {
      setState((prev) => ({
        ...(prev ?? ({} as CDDAgentState)),
        errors: [...(prev?.errors ?? []), String(error)],
      }));
    }
  }, []);

  // Clear state and return to empty state
  const clearState = useCallback(() => {
    setState(null);
    setIsViewingPrevious(false);
    setIsRunning(false);
    sessionIdRef.current = null;
  }, []);

  // Cleanup on unmount
  useEffect(() => {
    return () => {
      if (eventSourceRef.current) {
        eventSourceRef.current.close();
      }
    };
  }, []);

  return {
    state,
    isRunning,
    isComplete,
    hasError,
    isViewingPrevious,
    pendingCheckpoint,
    currentPhase,
    streamingMessages,
    currentToolCall,
    generatedFiles,
    start,
    stop,
    loadAnalysis,
    fetchAnalyses,
    clearState,
    approveCheckpoint,
    rejectCheckpoint,
  };
}
