"use client";

import { PhaseProgress, PHASE_NAMES } from "@/lib/types";
import { Check, Clock, AlertCircle, Loader2 } from "lucide-react";

interface PhaseTimelineProps {
  phases: PhaseProgress[];
  currentPhase: number;
}

export function PhaseTimeline({ phases, currentPhase }: PhaseTimelineProps) {
  const getStatusIcon = (status: PhaseProgress["status"]) => {
    switch (status) {
      case "completed":
        return <Check className="w-4 h-4 text-green-400" />;
      case "in_progress":
        return <Loader2 className="w-4 h-4 text-blue-400 animate-spin" />;
      case "awaiting_approval":
        return <Clock className="w-4 h-4 text-yellow-400" />;
      case "error":
        return <AlertCircle className="w-4 h-4 text-red-400" />;
      default:
        return <div className="w-4 h-4 rounded-full bg-slate-600" />;
    }
  };

  const getStatusColor = (status: PhaseProgress["status"]) => {
    switch (status) {
      case "completed":
        return "bg-green-500";
      case "in_progress":
        return "bg-blue-500";
      case "awaiting_approval":
        return "bg-yellow-500";
      case "error":
        return "bg-red-500";
      default:
        return "bg-slate-600";
    }
  };

  return (
    <div className="space-y-2">
      <div className="flex justify-between text-xs text-slate-400 mb-1">
        <span>Progress</span>
        <span>Phase {currentPhase} of 6</span>
      </div>

      {/* Progress Bar */}
      <div className="relative h-2 bg-slate-700 rounded-full overflow-hidden">
        {phases.map((phase, idx) => {
          const width = 100 / 6;
          const left = idx * width;
          return (
            <div
              key={phase.phase_number}
              className={`absolute h-full transition-all duration-500 ${getStatusColor(phase.status)}`}
              style={{
                left: `${left}%`,
                width: `${width}%`,
                opacity: phase.status === "pending" ? 0.3 : 1,
              }}
            />
          );
        })}
      </div>

      {/* Phase Labels */}
      <div className="flex justify-between">
        {phases.map((phase) => (
          <div
            key={phase.phase_number}
            className={`flex flex-col items-center gap-1 flex-1 ${
              phase.phase_number === currentPhase ? "text-white" : "text-slate-500"
            }`}
          >
            <div className="flex items-center gap-1">
              {getStatusIcon(phase.status)}
              <span className="text-xs font-medium">
                {PHASE_NAMES[phase.phase_number] || `Phase ${phase.phase_number}`}
              </span>
            </div>
            {phase.status === "in_progress" && (
              <span className="text-[10px] text-slate-400">
                {phase.agents_completed}/{phase.agents_total} agents
              </span>
            )}
          </div>
        ))}
      </div>
    </div>
  );
}
