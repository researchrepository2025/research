"use client";

import { useState } from "react";
import { CheckpointData } from "@/lib/types";
import { X, Check, AlertCircle, FileText, Target, ClipboardList, Flag } from "lucide-react";

interface CheckpointModalProps {
  checkpoint: CheckpointData;
  onApprove: (feedback?: string) => void;
  onReject: (feedback?: string) => void;
}

export function CheckpointModal({ checkpoint, onApprove, onReject }: CheckpointModalProps) {
  const [feedback, setFeedback] = useState("");
  const [isSubmitting, setIsSubmitting] = useState(false);

  const getCheckpointIcon = () => {
    switch (checkpoint.checkpoint_type) {
      case "scope":
        return <Target className="w-6 h-6" />;
      case "findings":
        return <ClipboardList className="w-6 h-6" />;
      case "draft":
        return <FileText className="w-6 h-6" />;
      case "final":
        return <Flag className="w-6 h-6" />;
      default:
        return <AlertCircle className="w-6 h-6" />;
    }
  };

  const getCheckpointColor = () => {
    switch (checkpoint.checkpoint_type) {
      case "scope":
        return "text-blue-400 bg-blue-500/10 border-blue-500/30";
      case "findings":
        return "text-green-400 bg-green-500/10 border-green-500/30";
      case "draft":
        return "text-purple-400 bg-purple-500/10 border-purple-500/30";
      case "final":
        return "text-orange-400 bg-orange-500/10 border-orange-500/30";
      default:
        return "text-slate-400 bg-slate-500/10 border-slate-500/30";
    }
  };

  const handleApprove = async () => {
    setIsSubmitting(true);
    await onApprove(feedback || undefined);
  };

  const handleReject = async (customFeedback?: string) => {
    setIsSubmitting(true);
    await onReject(customFeedback || feedback || undefined);
  };

  const renderCheckpointContent = () => {
    const data = checkpoint.data as Record<string, unknown>;
    const marketDef = data.market_definition as string | undefined;
    const competitors = data.competitors as string[] | undefined;
    const focusAreas = data.focus_areas as string[] | undefined;
    const summary = data.summary as string | undefined;
    const keyFindings = data.key_findings as string[] | undefined;
    const coverageInfo = data.coverage as string | undefined;
    const sections = data.sections as Record<string, unknown> | undefined;
    const wordCount = data.word_count as number | undefined;

    switch (checkpoint.checkpoint_type) {
      case "scope":
        return (
          <div className="space-y-4">
            {marketDef && (
              <div>
                <h4 className="text-xs font-medium text-slate-400 mb-1">Market Definition</h4>
                <p className="text-sm text-white">{marketDef}</p>
              </div>
            )}
            {competitors && competitors.length > 0 && (
              <div>
                <h4 className="text-xs font-medium text-slate-400 mb-1">Competitor Set</h4>
                <div className="flex flex-wrap gap-2">
                  {competitors.map((comp, idx) => (
                    <span
                      key={idx}
                      className="px-2 py-1 bg-slate-700 rounded text-xs text-white"
                    >
                      {comp}
                    </span>
                  ))}
                </div>
              </div>
            )}
            {focusAreas && focusAreas.length > 0 && (
              <div>
                <h4 className="text-xs font-medium text-slate-400 mb-1">Focus Areas</h4>
                <ul className="list-disc list-inside text-sm text-slate-300 space-y-1">
                  {focusAreas.map((area, idx) => (
                    <li key={idx}>{area}</li>
                  ))}
                </ul>
              </div>
            )}
          </div>
        );

      case "findings":
        return (
          <div className="space-y-4">
            {summary && (
              <div>
                <h4 className="text-xs font-medium text-slate-400 mb-1">Summary</h4>
                <p className="text-sm text-white">{summary}</p>
              </div>
            )}
            {keyFindings && keyFindings.length > 0 && (
              <div>
                <h4 className="text-xs font-medium text-slate-400 mb-1">Key Findings</h4>
                <ul className="list-disc list-inside text-sm text-slate-300 space-y-1">
                  {keyFindings.slice(0, 5).map((finding, idx) => (
                    <li key={idx}>{finding}</li>
                  ))}
                </ul>
              </div>
            )}
            {coverageInfo && (
              <div>
                <h4 className="text-xs font-medium text-slate-400 mb-1">Coverage</h4>
                <p className="text-sm text-slate-300">{coverageInfo}</p>
              </div>
            )}
          </div>
        );

      case "draft":
      case "final":
        return (
          <div className="space-y-4">
            {sections && (
              <div>
                <h4 className="text-xs font-medium text-slate-400 mb-2">Report Sections</h4>
                <div className="space-y-2">
                  {Object.keys(sections).map((section) => (
                    <div
                      key={section}
                      className="flex items-center justify-between px-3 py-2 bg-slate-700/50 rounded"
                    >
                      <span className="text-sm text-white capitalize">
                        {section.replace(/_/g, " ")}
                      </span>
                      <Check className="w-4 h-4 text-green-400" />
                    </div>
                  ))}
                </div>
              </div>
            )}
            {wordCount && (
              <p className="text-xs text-slate-400">
                Total word count: {wordCount.toLocaleString()}
              </p>
            )}
          </div>
        );

      default:
        return (
          <div className="text-sm text-slate-300">
            <pre className="whitespace-pre-wrap overflow-auto max-h-48">
              {JSON.stringify(data, null, 2)}
            </pre>
          </div>
        );
    }
  };

  return (
    <div className="fixed inset-0 z-50 flex items-center justify-center">
      {/* Backdrop */}
      <div className="absolute inset-0 bg-black/60 backdrop-blur-sm" />

      {/* Modal */}
      <div className="relative w-full max-w-lg mx-4 bg-slate-900 border border-slate-700 rounded-xl shadow-2xl">
        {/* Header */}
        <div className={`flex items-center gap-3 px-6 py-4 border-b ${getCheckpointColor()}`}>
          {getCheckpointIcon()}
          <div className="flex-1">
            <h2 className="text-lg font-semibold text-white">{checkpoint.title}</h2>
            <p className="text-xs text-slate-400 capitalize">
              {checkpoint.checkpoint_type} Checkpoint
            </p>
          </div>
          <button
            onClick={() => handleReject("Dismissed")}
            className="p-1 hover:bg-slate-700 rounded"
            disabled={isSubmitting}
          >
            <X className="w-5 h-5 text-slate-400" />
          </button>
        </div>

        {/* Content */}
        <div className="px-6 py-4 max-h-96 overflow-y-auto">
          <p className="text-sm text-slate-300 mb-4">{checkpoint.description}</p>
          {renderCheckpointContent()}
        </div>

        {/* Feedback Input */}
        <div className="px-6 py-3 border-t border-slate-700">
          <label className="block text-xs text-slate-400 mb-1">
            Feedback (optional)
          </label>
          <textarea
            value={feedback}
            onChange={(e) => setFeedback(e.target.value)}
            placeholder="Add any comments or modifications..."
            className="w-full px-3 py-2 bg-slate-800 border border-slate-600 rounded-lg text-sm text-white placeholder-slate-500 focus:outline-none focus:border-blue-500 resize-none"
            rows={2}
            disabled={isSubmitting}
          />
        </div>

        {/* Actions */}
        <div className="flex justify-end gap-3 px-6 py-4 border-t border-slate-700">
          <button
            onClick={() => handleReject()}
            disabled={isSubmitting}
            className="px-4 py-2 text-sm font-medium text-red-400 hover:bg-red-500/10 border border-red-500/30 rounded-lg transition-colors disabled:opacity-50"
          >
            Reject & Stop
          </button>
          <button
            onClick={() => handleApprove()}
            disabled={isSubmitting}
            className="flex items-center gap-2 px-4 py-2 text-sm font-medium text-white bg-green-600 hover:bg-green-700 rounded-lg transition-colors disabled:opacity-50"
          >
            <Check className="w-4 h-4" />
            Approve & Continue
          </button>
        </div>
      </div>
    </div>
  );
}
