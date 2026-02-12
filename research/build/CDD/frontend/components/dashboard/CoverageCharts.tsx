"use client";

import { CoverageMetrics } from "@/lib/types";
import {
  RadialBarChart,
  RadialBar,
  ResponsiveContainer,
  PolarAngleAxis,
} from "recharts";

interface CoverageChartsProps {
  coverage: CoverageMetrics;
}

export function CoverageCharts({ coverage }: CoverageChartsProps) {
  const categories = [
    { name: "Market", key: "market" as const, color: "#3b82f6" },
    { name: "Customer", key: "customer" as const, color: "#22c55e" },
    { name: "Company", key: "company" as const, color: "#a855f7" },
    { name: "Competitor", key: "competitor" as const, color: "#f97316" },
  ];

  const overallCoverage =
    (coverage.market + coverage.customer + coverage.company + coverage.competitor) / 4;

  return (
    <div className="bg-slate-900 rounded-lg border border-slate-700 h-full flex flex-col">
      <div className="px-4 py-3 border-b border-slate-700">
        <h3 className="text-sm font-semibold text-white">Analysis Coverage</h3>
        <p className="text-xs text-slate-400">
          Overall: {Math.round(overallCoverage * 100)}%
        </p>
      </div>

      <div className="flex-1 p-4 space-y-4">
        {/* Radial Chart */}
        <div className="h-40">
          <ResponsiveContainer width="100%" height="100%">
            <RadialBarChart
              cx="50%"
              cy="50%"
              innerRadius="30%"
              outerRadius="100%"
              data={categories.map((cat) => ({
                name: cat.name,
                value: coverage[cat.key] * 100,
                fill: cat.color,
              }))}
              startAngle={90}
              endAngle={-270}
            >
              <PolarAngleAxis
                type="number"
                domain={[0, 100]}
                angleAxisId={0}
                tick={false}
              />
              <RadialBar
                dataKey="value"
                cornerRadius={4}
                background={{ fill: "#1e293b" }}
              />
            </RadialBarChart>
          </ResponsiveContainer>
        </div>

        {/* Category Breakdown */}
        <div className="space-y-3">
          {categories.map((cat) => (
            <div key={cat.key} className="space-y-1">
              <div className="flex items-center justify-between text-xs">
                <span className="text-slate-300">{cat.name}</span>
                <span className="text-slate-400">
                  {Math.round(coverage[cat.key] * 100)}%
                </span>
              </div>
              <div className="h-2 bg-slate-700 rounded-full overflow-hidden">
                <div
                  className="h-full rounded-full transition-all duration-500"
                  style={{
                    width: `${coverage[cat.key] * 100}%`,
                    backgroundColor: cat.color,
                  }}
                />
              </div>
            </div>
          ))}
        </div>

        {/* Legend */}
        <div className="pt-2 border-t border-slate-700">
          <div className="grid grid-cols-2 gap-2">
            {categories.map((cat) => (
              <div key={cat.key} className="flex items-center gap-2">
                <div
                  className="w-2 h-2 rounded-full"
                  style={{ backgroundColor: cat.color }}
                />
                <span className="text-[10px] text-slate-400">{cat.name}</span>
              </div>
            ))}
          </div>
        </div>
      </div>
    </div>
  );
}
