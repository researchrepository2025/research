"use client";

import { AgentProgress, LAYER_COLORS } from "@/lib/types";
import { Loader2, Check, AlertCircle } from "lucide-react";

interface AgentStatusGridProps {
  activeAgents: AgentProgress[];
  completedAgents: AgentProgress[];
}

export function AgentStatusGrid({ activeAgents, completedAgents }: AgentStatusGridProps) {
  const getStatusIcon = (status: AgentProgress["status"]) => {
    switch (status) {
      case "running":
        return <Loader2 className="w-3 h-3 animate-spin" />;
      case "completed":
        return <Check className="w-3 h-3" />;
      case "error":
        return <AlertCircle className="w-3 h-3" />;
      default:
        return null;
    }
  };

  const formatAgentName = (name: string) => {
    return name
      .replace(/_/g, " ")
      .replace(/agent$/i, "")
      .trim();
  };

  return (
    <div className="bg-slate-900 rounded-lg border border-slate-700 h-full flex flex-col">
      <div className="px-4 py-3 border-b border-slate-700">
        <h3 className="text-sm font-semibold text-white">Agent Status</h3>
        <p className="text-xs text-slate-400">
          {activeAgents.length} active · {completedAgents.length} completed
        </p>
      </div>

      <div className="flex-1 overflow-y-auto p-2 space-y-2">
        {/* Active Agents */}
        {activeAgents.length > 0 && (
          <div className="space-y-1">
            <div className="text-xs font-medium text-slate-400 px-2">Running</div>
            {activeAgents.map((agent) => (
              <div
                key={agent.agent_name}
                className={`flex items-center gap-2 px-3 py-2 rounded-md border ${
                  LAYER_COLORS[agent.layer] || "border-slate-600 bg-slate-800/50"
                }`}
              >
                <div className="text-blue-400">
                  {getStatusIcon(agent.status)}
                </div>
                <div className="flex-1 min-w-0">
                  <div className="text-xs font-medium text-white truncate">
                    {formatAgentName(agent.agent_name)}
                  </div>
                  {agent.message && (
                    <div className="text-[10px] text-slate-400 truncate">
                      {agent.message}
                    </div>
                  )}
                </div>
                <span className="text-[10px] text-slate-500 capitalize">
                  {agent.layer}
                </span>
              </div>
            ))}
          </div>
        )}

        {/* Recently Completed */}
        {completedAgents.length > 0 && (
          <div className="space-y-1">
            <div className="text-xs font-medium text-slate-400 px-2">
              Completed ({completedAgents.length})
            </div>
            <div className="max-h-48 overflow-y-auto space-y-1">
              {completedAgents.slice(-10).reverse().map((agent) => (
                <div
                  key={agent.agent_name}
                  className="flex items-center gap-2 px-3 py-1.5 rounded-md bg-slate-800/30"
                >
                  <div className="text-green-400">
                    {getStatusIcon(agent.status)}
                  </div>
                  <div className="flex-1 min-w-0">
                    <div className="text-xs text-slate-400 truncate">
                      {formatAgentName(agent.agent_name)}
                    </div>
                  </div>
                  {agent.findings_count > 0 && (
                    <span className="text-[10px] text-green-400">
                      {agent.findings_count} findings
                    </span>
                  )}
                </div>
              ))}
            </div>
          </div>
        )}

        {/* Empty State */}
        {activeAgents.length === 0 && completedAgents.length === 0 && (
          <div className="flex items-center justify-center h-full text-slate-500 text-sm">
            No agents running
          </div>
        )}
      </div>
    </div>
  );
}
