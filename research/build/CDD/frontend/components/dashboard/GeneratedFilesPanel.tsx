"use client";

import { useState } from "react";
import {
  FileText,
  FileCode,
  FileJson,
  ChevronDown,
  ChevronRight,
  Clock,
  HardDrive,
  Bot,
  X,
} from "lucide-react";
import type { GeneratedFile } from "@/lib/types";

interface GeneratedFilesPanelProps {
  files: GeneratedFile[];
}

// Get icon based on file type
function getFileIcon(fileType: string) {
  switch (fileType) {
    case "markdown":
      return <FileText className="w-4 h-4 text-blue-400" />;
    case "json":
      return <FileJson className="w-4 h-4 text-yellow-400" />;
    case "code":
      return <FileCode className="w-4 h-4 text-green-400" />;
    default:
      return <FileText className="w-4 h-4 text-slate-400" />;
  }
}

// Format file size
function formatSize(bytes: number): string {
  if (bytes < 1024) return `${bytes} B`;
  if (bytes < 1024 * 1024) return `${(bytes / 1024).toFixed(1)} KB`;
  return `${(bytes / (1024 * 1024)).toFixed(1)} MB`;
}

// Format agent name
function formatAgentName(name: string | null): string {
  if (!name) return "Unknown";
  return name
    .replace(/-/g, " ")
    .replace(/agent$/, "")
    .trim()
    .split(" ")
    .map((word) => word.charAt(0).toUpperCase() + word.slice(1))
    .join(" ");
}

export function GeneratedFilesPanel({ files }: GeneratedFilesPanelProps) {
  const [expandedFile, setExpandedFile] = useState<string | null>(null);
  const [previewFile, setPreviewFile] = useState<GeneratedFile | null>(null);

  const toggleExpand = (fileId: string) => {
    setExpandedFile(expandedFile === fileId ? null : fileId);
  };

  return (
    <div className="bg-slate-800/50 rounded-lg border border-slate-700 h-full flex flex-col">
      {/* Header */}
      <div className="flex items-center justify-between px-4 py-3 border-b border-slate-700">
        <div className="flex items-center gap-2">
          <FileText className="w-4 h-4 text-purple-400" />
          <h3 className="text-sm font-medium text-white">Generated Files</h3>
        </div>
        <span className="text-xs text-slate-400">{files.length} files</span>
      </div>

      {/* File List */}
      <div className="flex-1 overflow-y-auto p-2">
        {files.length === 0 ? (
          <div className="flex flex-col items-center justify-center h-full text-slate-500">
            <FileText className="w-8 h-8 mb-2 opacity-50" />
            <p className="text-xs">No files generated yet</p>
          </div>
        ) : (
          <div className="space-y-1">
            {files.map((file) => (
              <div
                key={file.id}
                className="bg-slate-900/50 rounded border border-slate-700 overflow-hidden"
              >
                {/* File Header */}
                <button
                  onClick={() => toggleExpand(file.id)}
                  className="w-full flex items-center gap-2 px-3 py-2 hover:bg-slate-700/50 transition-colors"
                >
                  {expandedFile === file.id ? (
                    <ChevronDown className="w-3 h-3 text-slate-400" />
                  ) : (
                    <ChevronRight className="w-3 h-3 text-slate-400" />
                  )}
                  {getFileIcon(file.file_type)}
                  <span className="text-xs text-white font-medium truncate flex-1 text-left">
                    {file.filename}
                  </span>
                  <span className="text-[10px] text-slate-500">
                    {formatSize(file.size)}
                  </span>
                </button>

                {/* Expanded Details */}
                {expandedFile === file.id && (
                  <div className="px-3 py-2 border-t border-slate-700 bg-slate-900/30">
                    {/* Metadata */}
                    <div className="flex flex-wrap gap-3 text-[10px] text-slate-400 mb-2">
                      <div className="flex items-center gap-1">
                        <HardDrive className="w-3 h-3" />
                        <span className="truncate max-w-[150px]" title={file.file_path}>
                          {file.file_path}
                        </span>
                      </div>
                      <div className="flex items-center gap-1">
                        <Clock className="w-3 h-3" />
                        <span>
                          {new Date(file.created_at).toLocaleTimeString()}
                        </span>
                      </div>
                      {file.agent && (
                        <div className="flex items-center gap-1">
                          <Bot className="w-3 h-3" />
                          <span>{formatAgentName(file.agent)}</span>
                        </div>
                      )}
                    </div>

                    {/* Preview */}
                    <div className="bg-slate-800 rounded p-2 mb-2">
                      <pre className="text-[10px] text-slate-300 whitespace-pre-wrap font-mono leading-relaxed max-h-32 overflow-y-auto">
                        {file.preview}
                      </pre>
                    </div>

                    {/* Actions */}
                    <div className="flex gap-2">
                      <button
                        onClick={() => setPreviewFile(file)}
                        className="px-2 py-1 text-[10px] bg-blue-600/20 text-blue-400 rounded hover:bg-blue-600/30 transition-colors"
                      >
                        Full Preview
                      </button>
                    </div>
                  </div>
                )}
              </div>
            ))}
          </div>
        )}
      </div>

      {/* Full Preview Modal */}
      {previewFile && (
        <div className="fixed inset-0 bg-black/80 flex items-center justify-center z-50 p-4">
          <div className="bg-slate-800 rounded-lg border border-slate-600 w-full max-w-4xl max-h-[80vh] flex flex-col">
            {/* Modal Header */}
            <div className="flex items-center justify-between px-4 py-3 border-b border-slate-700">
              <div className="flex items-center gap-2">
                {getFileIcon(previewFile.file_type)}
                <span className="text-sm font-medium text-white">
                  {previewFile.filename}
                </span>
              </div>
              <button
                onClick={() => setPreviewFile(null)}
                className="p-1 hover:bg-slate-700 rounded transition-colors"
              >
                <X className="w-4 h-4 text-slate-400" />
              </button>
            </div>

            {/* Modal Content */}
            <div className="flex-1 overflow-auto p-4">
              <pre className="text-xs text-slate-300 whitespace-pre-wrap font-mono leading-relaxed">
                {previewFile.preview}
                {previewFile.preview.endsWith("...") && (
                  <span className="text-slate-500 block mt-4">
                    [Preview truncated - full content available on disk]
                  </span>
                )}
              </pre>
            </div>

            {/* Modal Footer */}
            <div className="px-4 py-3 border-t border-slate-700 flex items-center justify-between">
              <div className="text-xs text-slate-400">
                {previewFile.file_path}
              </div>
              <button
                onClick={() => setPreviewFile(null)}
                className="px-3 py-1.5 text-xs bg-slate-700 text-white rounded hover:bg-slate-600 transition-colors"
              >
                Close
              </button>
            </div>
          </div>
        </div>
      )}
    </div>
  );
}
