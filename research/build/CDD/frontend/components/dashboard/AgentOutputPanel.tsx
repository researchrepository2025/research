"use client";

import { useEffect, useRef } from "react";
import { Terminal, Bot, Loader2 } from "lucide-react";
import type { StreamingMessage, CurrentToolCall } from "@/lib/types";

interface AgentOutputPanelProps {
  messages: StreamingMessage[];
  currentToolCall: CurrentToolCall | null;
}

// Format agent name for display
function formatAgentName(name: string): string {
  return name
    .replace(/-/g, " ")
    .replace(/agent$/, "")
    .trim()
    .split(" ")
    .map((word) => word.charAt(0).toUpperCase() + word.slice(1))
    .join(" ");
}

export function AgentOutputPanel({
  messages,
  currentToolCall,
}: AgentOutputPanelProps) {
  const scrollRef = useRef<HTMLDivElement>(null);

  // Auto-scroll to bottom when new messages arrive
  useEffect(() => {
    if (scrollRef.current) {
      scrollRef.current.scrollTop = scrollRef.current.scrollHeight;
    }
  }, [messages]);

  return (
    <div className="bg-slate-800/50 rounded-lg border border-slate-700 h-full flex flex-col">
      {/* Header */}
      <div className="flex items-center justify-between px-4 py-3 border-b border-slate-700">
        <div className="flex items-center gap-2">
          <Terminal className="w-4 h-4 text-green-400" />
          <h3 className="text-sm font-medium text-white">Agent Output</h3>
        </div>
        {currentToolCall && (
          <div className="flex items-center gap-2 text-xs">
            <Loader2 className="w-3 h-3 animate-spin text-blue-400" />
            <span className="text-blue-400">
              {formatAgentName(currentToolCall.agent)}
            </span>
          </div>
        )}
      </div>

      {/* Messages */}
      <div
        ref={scrollRef}
        className="flex-1 overflow-y-auto p-4 space-y-3 font-mono text-xs"
      >
        {messages.length === 0 ? (
          <div className="flex flex-col items-center justify-center h-full text-slate-500">
            <Bot className="w-8 h-8 mb-2 opacity-50" />
            <p>Waiting for agent output...</p>
          </div>
        ) : (
          messages.map((msg) => (
            <div
              key={msg.id}
              className="animate-fade-in"
            >
              {/* Agent label */}
              <div className="flex items-center gap-2 mb-1">
                <span className="text-[10px] px-1.5 py-0.5 rounded bg-slate-700 text-slate-400">
                  {formatAgentName(msg.agent)}
                </span>
                <span className="text-[10px] text-slate-600">
                  {new Date(msg.timestamp).toLocaleTimeString()}
                </span>
              </div>
              {/* Message content */}
              <div className="text-slate-300 leading-relaxed whitespace-pre-wrap pl-2 border-l-2 border-slate-700">
                {msg.content.length > 500
                  ? msg.content.slice(0, 500) + "..."
                  : msg.content}
              </div>
            </div>
          ))
        )}
      </div>

      {/* Active tool indicator */}
      {currentToolCall && (
        <div className="px-4 py-2 border-t border-slate-700 bg-slate-900/50">
          <div className="flex items-center gap-2 text-xs text-slate-400">
            <div className="w-2 h-2 rounded-full bg-green-500 animate-pulse" />
            <span>
              Running: <span className="text-white">{formatAgentName(currentToolCall.agent)}</span>
            </span>
          </div>
        </div>
      )}
    </div>
  );
}
