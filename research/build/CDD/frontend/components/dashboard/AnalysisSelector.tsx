"use client";

import { useState, useEffect } from "react";
import { Folder, FileText, Clock, HardDrive, RefreshCw } from "lucide-react";
import type { PreviousAnalysis } from "@/lib/types";

interface AnalysisSelectorProps {
  onSelect: (companyName: string) => void;
  fetchAnalyses: () => Promise<PreviousAnalysis[]>;
}

function formatSize(bytes: number): string {
  if (bytes < 1024) return `${bytes} B`;
  if (bytes < 1024 * 1024) return `${(bytes / 1024).toFixed(1)} KB`;
  return `${(bytes / (1024 * 1024)).toFixed(1)} MB`;
}

function formatDate(dateStr: string): string {
  const date = new Date(dateStr);
  const now = new Date();
  const diffMs = now.getTime() - date.getTime();
  const diffDays = Math.floor(diffMs / (1000 * 60 * 60 * 24));

  if (diffDays === 0) {
    return `Today at ${date.toLocaleTimeString([], { hour: "2-digit", minute: "2-digit" })}`;
  } else if (diffDays === 1) {
    return "Yesterday";
  } else if (diffDays < 7) {
    return `${diffDays} days ago`;
  } else {
    return date.toLocaleDateString();
  }
}

export function AnalysisSelector({ onSelect, fetchAnalyses }: AnalysisSelectorProps) {
  const [analyses, setAnalyses] = useState<PreviousAnalysis[]>([]);
  const [isLoading, setIsLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);

  const loadAnalyses = async () => {
    setIsLoading(true);
    setError(null);
    try {
      const data = await fetchAnalyses();
      setAnalyses(data);
    } catch {
      setError("Failed to load previous analyses");
    } finally {
      setIsLoading(false);
    }
  };

  useEffect(() => {
    loadAnalyses();
  }, [fetchAnalyses]);

  if (isLoading) {
    return (
      <div className="flex items-center justify-center py-8">
        <RefreshCw className="w-5 h-5 text-slate-400 animate-spin" />
        <span className="ml-2 text-slate-400 text-sm">Loading previous analyses...</span>
      </div>
    );
  }

  if (error) {
    return (
      <div className="text-center py-8">
        <p className="text-red-400 text-sm mb-2">{error}</p>
        <button
          onClick={loadAnalyses}
          className="text-blue-400 hover:text-blue-300 text-sm underline"
        >
          Try again
        </button>
      </div>
    );
  }

  if (analyses.length === 0) {
    return (
      <div className="text-center py-8 text-slate-500">
        <Folder className="w-8 h-8 mx-auto mb-2 opacity-50" />
        <p className="text-sm">No previous analyses found</p>
      </div>
    );
  }

  return (
    <div className="space-y-4">
      <div className="flex items-center justify-between">
        <h3 className="text-sm font-medium text-slate-300">Previous Analyses</h3>
        <button
          onClick={loadAnalyses}
          className="p-1 hover:bg-slate-700 rounded transition-colors"
          title="Refresh"
        >
          <RefreshCw className="w-4 h-4 text-slate-400" />
        </button>
      </div>

      <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-3 max-h-64 overflow-y-auto">
        {analyses.map((analysis) => (
          <button
            key={analysis.directory_path}
            onClick={() => onSelect(analysis.company_name)}
            className="flex flex-col p-3 bg-slate-800/50 hover:bg-slate-700/50 border border-slate-700 hover:border-slate-600 rounded-lg text-left transition-colors group"
          >
            <div className="flex items-start justify-between gap-2 mb-2">
              <div className="flex items-center gap-2 min-w-0">
                <Folder className="w-4 h-4 text-blue-400 flex-shrink-0" />
                <span className="text-sm font-medium text-white truncate">
                  {analysis.company_name}
                </span>
              </div>
              {analysis.has_report && (
                <span className="px-1.5 py-0.5 text-[10px] bg-green-600/20 text-green-400 rounded flex-shrink-0">
                  Report
                </span>
              )}
            </div>

            <div className="flex flex-wrap gap-x-3 gap-y-1 text-[10px] text-slate-400">
              <div className="flex items-center gap-1">
                <FileText className="w-3 h-3" />
                <span>{analysis.file_count} files</span>
              </div>
              <div className="flex items-center gap-1">
                <HardDrive className="w-3 h-3" />
                <span>{formatSize(analysis.total_size)}</span>
              </div>
              <div className="flex items-center gap-1">
                <Clock className="w-3 h-3" />
                <span>{formatDate(analysis.last_modified)}</span>
              </div>
            </div>
          </button>
        ))}
      </div>
    </div>
  );
}
