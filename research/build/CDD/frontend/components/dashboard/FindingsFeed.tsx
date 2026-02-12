"use client";

import { useEffect, useRef } from "react";
import { Finding, CATEGORY_COLORS, LAYER_COLORS } from "@/lib/types";
import { ExternalLink, Clock } from "lucide-react";

interface FindingsFeedProps {
  findings: Finding[];
}

export function FindingsFeed({ findings }: FindingsFeedProps) {
  const feedRef = useRef<HTMLDivElement>(null);

  // Auto-scroll to bottom when new findings arrive
  useEffect(() => {
    if (feedRef.current) {
      feedRef.current.scrollTop = feedRef.current.scrollHeight;
    }
  }, [findings.length]);

  const formatTimestamp = (timestamp: string) => {
    const date = new Date(timestamp);
    return date.toLocaleTimeString("en-US", {
      hour: "2-digit",
      minute: "2-digit",
      second: "2-digit",
    });
  };

  const formatAgentName = (name: string) => {
    return name
      .replace(/_/g, " ")
      .replace(/agent$/i, "")
      .trim();
  };

  return (
    <div className="bg-slate-900 rounded-lg border border-slate-700 h-full flex flex-col">
      <div className="px-4 py-3 border-b border-slate-700 flex items-center justify-between">
        <div>
          <h3 className="text-sm font-semibold text-white">Research Findings</h3>
          <p className="text-xs text-slate-400">{findings.length} findings collected</p>
        </div>
        <div className="flex gap-1">
          {(["market", "customer", "company", "competitor"] as const).map((cat) => (
            <span
              key={cat}
              className={`px-2 py-0.5 rounded text-[10px] font-medium ${CATEGORY_COLORS[cat]}`}
            >
              {findings.filter((f) => f.category === cat).length}
            </span>
          ))}
        </div>
      </div>

      <div ref={feedRef} className="flex-1 overflow-y-auto p-3 space-y-3">
        {findings.length === 0 ? (
          <div className="flex items-center justify-center h-full text-slate-500 text-sm">
            Findings will appear here as agents complete their research
          </div>
        ) : (
          findings.map((finding) => (
            <div
              key={finding.id}
              className={`p-3 rounded-lg border animate-slide-in ${
                LAYER_COLORS[finding.layer] || "border-slate-600 bg-slate-800/50"
              }`}
            >
              {/* Header */}
              <div className="flex items-start justify-between gap-2 mb-2">
                <div className="flex items-center gap-2">
                  <span
                    className={`px-2 py-0.5 rounded text-[10px] font-medium ${
                      CATEGORY_COLORS[finding.category]
                    }`}
                  >
                    {finding.category}
                  </span>
                  <span className="text-xs text-slate-400">
                    {formatAgentName(finding.agent)}
                  </span>
                </div>
                <div className="flex items-center gap-1 text-[10px] text-slate-500">
                  <Clock className="w-3 h-3" />
                  {formatTimestamp(finding.timestamp)}
                </div>
              </div>

              {/* Title */}
              <h4 className="text-sm font-medium text-white mb-1">{finding.title}</h4>

              {/* Content */}
              <p className="text-xs text-slate-300 leading-relaxed mb-2">
                {finding.content}
              </p>

              {/* Footer */}
              <div className="flex items-center justify-between">
                {/* Sources */}
                {finding.sources.length > 0 && (
                  <div className="flex items-center gap-1 flex-wrap">
                    {finding.sources.slice(0, 3).map((source, idx) => (
                      <a
                        key={idx}
                        href={source}
                        target="_blank"
                        rel="noopener noreferrer"
                        className="flex items-center gap-1 text-[10px] text-blue-400 hover:text-blue-300"
                      >
                        <ExternalLink className="w-3 h-3" />
                        Source {idx + 1}
                      </a>
                    ))}
                    {finding.sources.length > 3 && (
                      <span className="text-[10px] text-slate-500">
                        +{finding.sources.length - 3} more
                      </span>
                    )}
                  </div>
                )}

                {/* Confidence */}
                {finding.confidence !== null && (
                  <div className="flex items-center gap-1">
                    <div className="w-12 h-1.5 bg-slate-700 rounded-full overflow-hidden">
                      <div
                        className={`h-full rounded-full ${
                          finding.confidence >= 0.7
                            ? "bg-green-500"
                            : finding.confidence >= 0.4
                            ? "bg-yellow-500"
                            : "bg-red-500"
                        }`}
                        style={{ width: `${finding.confidence * 100}%` }}
                      />
                    </div>
                    <span className="text-[10px] text-slate-400">
                      {Math.round(finding.confidence * 100)}%
                    </span>
                  </div>
                )}
              </div>
            </div>
          ))
        )}
      </div>
    </div>
  );
}
