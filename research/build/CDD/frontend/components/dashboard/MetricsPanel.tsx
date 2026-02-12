"use client";

import { CDDAgentState } from "@/lib/types";
import { Clock, Users, FileText, CheckCircle, AlertTriangle } from "lucide-react";

interface MetricsPanelProps {
  state: CDDAgentState;
}

export function MetricsPanel({ state }: MetricsPanelProps) {
  const elapsed = () => {
    const start = new Date(state.started_at);
    const now = new Date();
    const diff = Math.floor((now.getTime() - start.getTime()) / 1000);
    const mins = Math.floor(diff / 60);
    const secs = diff % 60;
    return `${mins}:${secs.toString().padStart(2, "0")}`;
  };

  const totalAgents = state.active_agents.length + state.completed_agents.length;
  const checkpointsPassed = state.checkpoint_history.filter((c) => c.approved).length;

  const metrics = [
    {
      label: "Elapsed Time",
      value: elapsed(),
      icon: Clock,
      color: "text-blue-400",
    },
    {
      label: "Active Agents",
      value: `${state.active_agents.length}`,
      subValue: `/ ${totalAgents} total`,
      icon: Users,
      color: "text-green-400",
    },
    {
      label: "Findings",
      value: state.findings.length.toString(),
      icon: FileText,
      color: "text-purple-400",
    },
    {
      label: "Checkpoints",
      value: `${checkpointsPassed}/4`,
      icon: CheckCircle,
      color: "text-yellow-400",
    },
  ];

  return (
    <div className="bg-slate-900 rounded-lg border border-slate-700">
      <div className="px-4 py-3 border-b border-slate-700">
        <h3 className="text-sm font-semibold text-white">Metrics</h3>
      </div>

      <div className="p-3 grid grid-cols-2 gap-3">
        {metrics.map((metric) => (
          <div
            key={metric.label}
            className="p-3 bg-slate-800/50 rounded-lg border border-slate-700"
          >
            <div className="flex items-center gap-2 mb-1">
              <metric.icon className={`w-4 h-4 ${metric.color}`} />
              <span className="text-[10px] text-slate-400">{metric.label}</span>
            </div>
            <div className="flex items-baseline gap-1">
              <span className="text-lg font-semibold text-white">{metric.value}</span>
              {metric.subValue && (
                <span className="text-xs text-slate-500">{metric.subValue}</span>
              )}
            </div>
          </div>
        ))}
      </div>

      {/* Errors Section */}
      {state.errors.length > 0 && (
        <div className="px-3 pb-3">
          <div className="p-2 bg-red-500/10 border border-red-500/30 rounded-lg">
            <div className="flex items-center gap-2 text-red-400 mb-1">
              <AlertTriangle className="w-4 h-4" />
              <span className="text-xs font-medium">
                {state.errors.length} Error{state.errors.length > 1 ? "s" : ""}
              </span>
            </div>
            <p className="text-[10px] text-red-300 truncate">
              {state.errors[state.errors.length - 1]}
            </p>
          </div>
        </div>
      )}
    </div>
  );
}
