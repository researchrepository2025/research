"use client";

import { useState } from "react";
import { useCDDAgent } from "@/hooks/useCDDAgent";
import { PhaseTimeline } from "./PhaseTimeline";
import { AgentStatusGrid } from "./AgentStatusGrid";
import { FindingsFeed } from "./FindingsFeed";
import { CoverageCharts } from "./CoverageCharts";
import { MetricsPanel } from "./MetricsPanel";
import { AgentOutputPanel } from "./AgentOutputPanel";
import { GeneratedFilesPanel } from "./GeneratedFilesPanel";
import { CheckpointModal } from "../checkpoints/CheckpointModal";
import { AnalysisSelector } from "./AnalysisSelector";
import { Play, Square, FileText, AlertCircle, ArrowLeft } from "lucide-react";

export function CDDDashboard() {
  const [companyName, setCompanyName] = useState("");
  const {
    state,
    isRunning,
    isComplete,
    hasError,
    isViewingPrevious,
    pendingCheckpoint,
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
  } = useCDDAgent();

  const handleStart = async () => {
    if (companyName.trim()) {
      await start(companyName.trim());
    }
  };

  return (
    <div className="flex flex-col h-screen">
      {/* Header */}
      <header className="flex items-center justify-between px-6 py-4 bg-slate-900 border-b border-slate-700">
        <div className="flex items-center gap-4">
          {(state || isViewingPrevious) && (
            <button
              onClick={clearState}
              className="p-2 hover:bg-slate-700 rounded-lg transition-colors"
              title="Back to home"
            >
              <ArrowLeft className="w-5 h-5 text-slate-400" />
            </button>
          )}
          <h1 className="text-xl font-bold text-white">CDD Analysis</h1>
          {state && (
            <span className="text-slate-400">
              {isViewingPrevious ? "Viewing:" : "Analyzing:"}{" "}
              <span className="text-white font-medium">{state.company_name}</span>
              {isViewingPrevious && (
                <span className="ml-2 px-2 py-0.5 text-xs bg-blue-600/20 text-blue-400 rounded">
                  Previous
                </span>
              )}
            </span>
          )}
        </div>

        <div className="flex items-center gap-3">
          {!isRunning && !state && (
            <>
              <input
                type="text"
                placeholder="Enter company name..."
                value={companyName}
                onChange={(e) => setCompanyName(e.target.value)}
                onKeyDown={(e) => e.key === "Enter" && handleStart()}
                className="px-4 py-2 bg-slate-800 border border-slate-600 rounded-lg text-white placeholder-slate-400 focus:outline-none focus:border-blue-500 w-64"
              />
              <button
                onClick={handleStart}
                disabled={!companyName.trim()}
                className="flex items-center gap-2 px-4 py-2 bg-green-600 hover:bg-green-700 disabled:bg-slate-600 disabled:cursor-not-allowed rounded-lg text-white font-medium transition-colors"
              >
                <Play className="w-4 h-4" />
                Start Analysis
              </button>
            </>
          )}

          {isRunning && (
            <button
              onClick={stop}
              className="flex items-center gap-2 px-4 py-2 bg-red-600 hover:bg-red-700 rounded-lg text-white font-medium transition-colors"
            >
              <Square className="w-4 h-4" />
              Stop
            </button>
          )}

          {isComplete && (
            <button className="flex items-center gap-2 px-4 py-2 bg-blue-600 hover:bg-blue-700 rounded-lg text-white font-medium transition-colors">
              <FileText className="w-4 h-4" />
              View Report
            </button>
          )}

          {hasError && (
            <div className="flex items-center gap-2 text-red-400">
              <AlertCircle className="w-5 h-5" />
              <span>Errors occurred</span>
            </div>
          )}
        </div>
      </header>

      {/* Phase Timeline - Full Width */}
      {state && (
        <div className="px-6 py-4 bg-slate-900/50 border-b border-slate-700">
          <PhaseTimeline phases={state.phases} currentPhase={state.current_phase} />
        </div>
      )}

      {/* Main Content Grid */}
      <div className="flex-1 overflow-hidden">
        {!state ? (
          // Empty State with Analysis Selector
          <div className="flex items-center justify-center h-full">
            <div className="w-full max-w-2xl px-6">
              <div className="text-center mb-8">
                <h2 className="text-2xl font-semibold text-slate-300 mb-2">
                  Commercial Due Diligence Analysis
                </h2>
                <p className="text-slate-500">
                  Enter a company name above to start a new analysis, or select a previous one below.
                </p>
              </div>

              {/* Previous Analyses */}
              <AnalysisSelector
                onSelect={loadAnalysis}
                fetchAnalyses={fetchAnalyses}
              />
            </div>
          </div>
        ) : (
          // Dashboard Grid - 4 columns
          <div className="grid grid-cols-12 gap-3 p-4 h-full overflow-hidden">
            {/* Column 1 - Metrics & Agent Status */}
            <div className="col-span-2 flex flex-col gap-3 overflow-hidden">
              <MetricsPanel state={state} />
              <div className="flex-1 overflow-hidden">
                <AgentStatusGrid
                  activeAgents={state.active_agents}
                  completedAgents={state.completed_agents}
                />
              </div>
            </div>

            {/* Column 2 - Live Agent Output */}
            <div className="col-span-4 overflow-hidden">
              <AgentOutputPanel
                messages={streamingMessages}
                currentToolCall={currentToolCall}
              />
            </div>

            {/* Column 3 - Findings Feed */}
            <div className="col-span-3 overflow-hidden">
              <FindingsFeed findings={state.findings} />
            </div>

            {/* Column 4 - Files & Coverage */}
            <div className="col-span-3 flex flex-col gap-3 overflow-hidden">
              <div className="flex-1 overflow-hidden">
                <GeneratedFilesPanel files={generatedFiles} />
              </div>
              <CoverageCharts coverage={state.coverage} />
            </div>
          </div>
        )}
      </div>

      {/* Checkpoint Modal */}
      {pendingCheckpoint && (
        <CheckpointModal
          checkpoint={pendingCheckpoint}
          onApprove={(feedback) => approveCheckpoint(pendingCheckpoint.checkpoint_id, feedback)}
          onReject={(feedback) => rejectCheckpoint(pendingCheckpoint.checkpoint_id, feedback)}
        />
      )}
    </div>
  );
}
