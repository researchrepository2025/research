# Implementation Plan: Hybrid AI Architecture Evolution Visualization

## Executive Summary

This plan details the implementation of an interactive React visualization application that communicates the evolution from traditional siloed AI deployments to modern hybrid architectures. The visualization will be a "living, breathing" experience using React Flow for node-based diagrams and Framer Motion for animations.

**Deployment Target:** Standalone React web app (Vercel/Netlify)

**Core Messages:**
- Efficiency/Simplicity: Offloading dev tools reduces complexity while keeping value on-prem
- Interoperability: Everything needs to work together across all locations
- Security/Sovereignty is NOT one-size-fits-all (depends on industry, regulations, risk appetite, cost)

---

## 1. Project Structure

```
hybrid-ai-viz/
├── public/
│   └── favicon.ico
├── src/
│   ├── app/                          # Next.js App Router
│   │   ├── layout.tsx
│   │   ├── page.tsx                  # Main entry - scene selector
│   │   ├── traditional/
│   │   │   └── page.tsx              # Scene 1: Traditional World
│   │   ├── hybrid/
│   │   │   └── page.tsx              # Scene 2: Hybrid Reality
│   │   ├── isolated/
│   │   │   └── page.tsx              # Scene 3: Isolated Anti-Pattern
│   │   └── explorer/
│   │       └── page.tsx              # Interactive Explorer Mode
│   │
│   ├── components/
│   │   ├── flow/                     # React Flow components
│   │   │   ├── FlowCanvas.tsx        # Main React Flow wrapper
│   │   │   ├── nodes/                # Custom node components
│   │   │   │   ├── LocationNode.tsx  # Base location node
│   │   │   │   ├── PublicCloudNode.tsx
│   │   │   │   ├── VPCNode.tsx
│   │   │   │   ├── NeoCloudNode.tsx
│   │   │   │   ├── OnPremCloudOwnedNode.tsx
│   │   │   │   ├── SaaSVendorNode.tsx
│   │   │   │   ├── ColocationNode.tsx
│   │   │   │   ├── EnterpriseOnPremNode.tsx
│   │   │   │   ├── NearEdgeNode.tsx
│   │   │   │   ├── FarEdgeNode.tsx
│   │   │   │   └── FunctionalEdgeNode.tsx
│   │   │   ├── edges/                # Custom edge components
│   │   │   │   ├── AnimatedDataEdge.tsx
│   │   │   │   ├── ParticleEdge.tsx
│   │   │   │   └── DisconnectedEdge.tsx
│   │   │   └── controls/
│   │   │       ├── FilterControls.tsx
│   │   │       └── ViewControls.tsx
│   │   │
│   │   ├── scenes/                   # Scene-specific compositions
│   │   │   ├── TraditionalScene.tsx
│   │   │   ├── HybridScene.tsx
│   │   │   ├── IsolatedScene.tsx
│   │   │   └── ExplorerScene.tsx
│   │   │
│   │   ├── panels/                   # Detail panels
│   │   │   ├── NodeDetailPanel.tsx   # Click-to-reveal details
│   │   │   ├── ComponentList.tsx     # Components at a location
│   │   │   └── ConsequencePanel.tsx  # Anti-pattern consequences
│   │   │
│   │   ├── animations/               # Animation components
│   │   │   ├── DataParticle.tsx      # Animated data flow particle
│   │   │   ├── PulsingGlow.tsx       # Node activity indicator
│   │   │   ├── ConnectionBeam.tsx    # Edge connection animation
│   │   │   └── SceneTransition.tsx   # Between-scene transitions
│   │   │
│   │   ├── navigation/
│   │   │   ├── SceneNavigator.tsx    # Scene progression controls
│   │   │   ├── NarrativeProgress.tsx # Story progress indicator
│   │   │   └── ModeToggle.tsx        # Narrative vs Explorer toggle
│   │   │
│   │   └── ui/                       # Shared UI components
│   │       ├── Legend.tsx
│   │       ├── Tooltip.tsx
│   │       └── Card.tsx
│   │
│   ├── data/                         # Static data definitions
│   │   ├── locations.ts              # Location type definitions
│   │   ├── components.ts             # AI component definitions
│   │   ├── patterns.ts               # Traditional deployment patterns
│   │   ├── connections.ts            # Edge/connection definitions
│   │   └── scenes/                   # Scene-specific data
│   │       ├── traditional.ts
│   │       ├── hybrid.ts
│   │       └── isolated.ts
│   │
│   ├── hooks/                        # Custom React hooks
│   │   ├── useAnimatedEdges.ts       # Edge animation controller
│   │   ├── useSceneTransition.ts     # Scene change management
│   │   ├── useNodeDetails.ts         # Node selection & details
│   │   ├── useParticleSystem.ts      # Canvas particle management
│   │   └── useFilterState.ts         # Component/view filtering
│   │
│   ├── stores/                       # State management (Zustand)
│   │   ├── sceneStore.ts             # Current scene state
│   │   ├── filterStore.ts            # Active filters
│   │   └── selectionStore.ts         # Selected nodes/details
│   │
│   ├── types/                        # TypeScript types
│   │   ├── location.ts
│   │   ├── component.ts
│   │   ├── scene.ts
│   │   └── flow.ts
│   │
│   ├── utils/                        # Utility functions
│   │   ├── layoutCalculations.ts     # Node positioning algorithms
│   │   ├── particlePhysics.ts        # Particle movement calculations
│   │   └── colorSchemes.ts           # Theme/color utilities
│   │
│   └── styles/
│       ├── globals.css
│       └── flow-theme.css            # React Flow custom styling
│
├── package.json
├── tailwind.config.ts
├── tsconfig.json
├── next.config.js
└── README.md
```

---

## 2. Data Model / TypeScript Interfaces

### 2.1 Location Types

```typescript
// src/types/location.ts

export type LocationCategory = 
  | 'cloud'           // Public/private cloud resources
  | 'edge'            // Edge computing locations
  | 'enterprise'      // Enterprise-owned infrastructure
  | 'vendor';         // Third-party vendor locations

export type OwnershipType = 
  | 'cloud-owned'     // Owned by cloud provider
  | 'enterprise-owned'// Owned by enterprise
  | 'vendor-owned'    // Owned by SaaS/service vendor
  | 'colocation';     // Shared facility

export interface LocationType {
  id: string;
  name: string;
  shortName: string;
  category: LocationCategory;
  ownership: OwnershipType;
  description: string;
  icon: string;                    // Icon identifier
  color: string;                   // Primary color for node
  canHostLLMs: boolean;
  canHostSensitiveData: boolean;
  typicalLatency: 'ultra-low' | 'low' | 'medium' | 'high';
  examples: string[];              // Real-world examples
}

// Enumeration of all location types
export const LOCATION_TYPES = {
  PUBLIC_CLOUD: 'public-cloud',
  VPC: 'virtual-private-cloud',
  NEO_CLOUD: 'neo-cloud',
  ON_PREM_CLOUD_OWNED: 'on-prem-cloud-owned',
  SAAS_VENDOR: 'saas-vendor-dc',
  COLOCATION: 'colocation',
  ENTERPRISE_ON_PREM: 'enterprise-on-prem',
  NEAR_EDGE_CLOUD: 'near-edge-cloud',
  NEAR_EDGE_ENTERPRISE: 'near-edge-enterprise',
  NEAR_EDGE_OTHER: 'near-edge-other',
  FAR_EDGE_CLOUD: 'far-edge-cloud',
  FAR_EDGE_ENTERPRISE: 'far-edge-enterprise',
  FAR_EDGE_OTHER: 'far-edge-other',
  FUNCTIONAL_EDGE: 'functional-edge',
} as const;
```

### 2.2 Component Types

```typescript
// src/types/component.ts

export type ComponentCategory = 
  | 'ai-models'       // LLMs, SLMs, ML models
  | 'data'            // Data and IP
  | 'storage'         // Storage-intensive files
  | 'dev-tools'       // Developer tools
  | 'mlops'           // MLOps platforms
  | 'observability';  // Monitoring/observability

export type DeploymentConstraint = 
  | 'must-be-local'        // MUST be on-prem/local
  | 'can-be-offloaded'     // CAN be in cloud
  | 'flexible';            // No strong constraint

export interface AIComponent {
  id: string;
  name: string;
  category: ComponentCategory;
  description: string;
  icon: string;
  constraint: DeploymentConstraint;
  constraintReason: string;        // Why this constraint exists
  examples: string[];              // Specific tool/tech examples
  valueLevel: 'high' | 'medium' | 'low';  // Business value indicator
  complexityLevel: 'high' | 'medium' | 'low'; // Operational complexity
}

// Component definitions
export const COMPONENTS: Record<string, AIComponent> = {
  LLM: {
    id: 'llm',
    name: 'Large Language Models',
    category: 'ai-models',
    constraint: 'must-be-local',
    constraintReason: 'Inference latency, data sovereignty, IP protection',
    valueLevel: 'high',
    complexityLevel: 'high',
    icon: 'brain',
    description: 'Foundation models for language understanding and generation',
    examples: ['GPT-4', 'Claude', 'Llama', 'Gemini'],
  },
  SLM: {
    id: 'slm',
    name: 'Small Language Models',
    category: 'ai-models',
    constraint: 'must-be-local',
    constraintReason: 'Edge deployment, low latency, offline capability',
    valueLevel: 'high',
    complexityLevel: 'medium',
    icon: 'cpu',
    description: 'Compact models optimized for edge and embedded deployment',
    examples: ['Phi-3', 'Gemma', 'Mistral-7B'],
  },
  SENSITIVE_DATA: {
    id: 'sensitive-data',
    name: 'Sensitive Data & IP',
    category: 'data',
    constraint: 'must-be-local',
    constraintReason: 'Regulatory compliance, competitive advantage, data sovereignty',
    valueLevel: 'high',
    complexityLevel: 'medium',
    icon: 'shield',
    description: 'Customer PII, proprietary algorithms, trade secrets',
    examples: ['Customer PII', 'Proprietary algorithms', 'Trade secrets'],
  },
  STORAGE_FILES: {
    id: 'storage-files',
    name: 'Storage-Intensive Files',
    category: 'storage',
    constraint: 'must-be-local',
    constraintReason: 'Data gravity, egress costs, latency for large files',
    valueLevel: 'medium',
    complexityLevel: 'low',
    icon: 'database',
    description: 'Large datasets, training data, model checkpoints',
    examples: ['Training datasets', 'Model checkpoints', 'Vector embeddings'],
  },
  DEV_TOOLS: {
    id: 'dev-tools',
    name: 'Developer Tools',
    category: 'dev-tools',
    constraint: 'can-be-offloaded',
    constraintReason: 'No sensitive data processed, benefits from cloud scalability and collaboration',
    valueLevel: 'medium',
    complexityLevel: 'high',
    icon: 'code',
    description: 'Development environments that point to on-prem infrastructure',
    examples: ['IDEs', 'Notebooks', 'CI/CD pipelines', 'Code repositories'],
  },
  MLOPS: {
    id: 'mlops',
    name: 'MLOps Platforms',
    category: 'mlops',
    constraint: 'can-be-offloaded',
    constraintReason: 'Operational tool that can orchestrate on-prem infrastructure remotely',
    valueLevel: 'medium',
    complexityLevel: 'high',
    icon: 'workflow',
    description: 'Model lifecycle management, experiment tracking, deployment orchestration',
    examples: ['MLflow', 'Kubeflow', 'SageMaker', 'Vertex AI', 'Weights & Biases'],
  },
  MONITORING: {
    id: 'monitoring',
    name: 'Monitoring & Observability',
    category: 'observability',
    constraint: 'can-be-offloaded',
    constraintReason: 'Aggregated metrics safe in cloud, benefits from cloud analytics',
    valueLevel: 'medium',
    complexityLevel: 'high',
    icon: 'activity',
    description: 'System health, model performance, drift detection, cost tracking',
    examples: ['Datadog', 'Grafana Cloud', 'Arize AI', 'WhyLabs'],
  },
};
```

### 2.3 Scene & Pattern Types

```typescript
// src/types/scene.ts

export type SceneId = 'traditional' | 'hybrid' | 'isolated' | 'explorer';

export type DeploymentPattern = 
  | 'buy-saas-hosted'      // Buy SaaS - Fully hosted by vendor
  | 'buy-saas-onprem'      // Buy SaaS - Fully on-prem
  | 'build-cloud'          // Build - Fully cloud
  | 'build-onprem';        // Build - Fully on-prem

export interface SceneConfig {
  id: SceneId;
  title: string;
  subtitle: string;
  description: string;
  keyMessage: string;
  nodes: SceneNode[];
  edges: SceneEdge[];
  animationConfig: AnimationConfig;
}

export interface SceneNode {
  id: string;
  locationType: string;           // References LOCATION_TYPES
  position: { x: number; y: number };
  components: string[];           // Component IDs hosted here
  isActive: boolean;              // Whether node is "alive" in this scene
  pattern?: DeploymentPattern;    // For traditional scene grouping
  highlight?: 'positive' | 'negative' | 'neutral';
}

export interface SceneEdge {
  id: string;
  source: string;
  target: string;
  animated: boolean;
  dataFlowType: 'data' | 'control' | 'model' | 'none';
  bidirectional: boolean;
  label?: string;
}

export interface AnimationConfig {
  particleSpeed: number;          // Data flow particle speed
  particleDensity: number;        // Particles per edge
  pulseInterval: number;          // Node pulse frequency (ms)
  enableParticles: boolean;
  enableGlow: boolean;
}
```

### 2.4 Flow Types (React Flow Integration)

```typescript
// src/types/flow.ts

import { Node, Edge, NodeProps } from '@xyflow/react';

export interface LocationNodeData {
  locationType: LocationType;
  components: AIComponent[];
  isActive: boolean;
  isHighlighted: boolean;
  highlightType?: 'positive' | 'negative' | 'neutral';
  onSelect: (nodeId: string) => void;
}

export type LocationNode = Node<LocationNodeData, 'location'>;

export interface DataEdgeData {
  dataFlowType: 'data' | 'control' | 'model' | 'none';
  isAnimated: boolean;
  particleColor?: string;
}

export type DataEdge = Edge<DataEdgeData>;

// Node type registry for React Flow
export const nodeTypes = {
  location: LocationNode,
  publicCloud: PublicCloudNode,
  vpc: VPCNode,
  neoCloud: NeoCloudNode,
  onPremCloudOwned: OnPremCloudOwnedNode,
  saasVendor: SaaSVendorNode,
  colocation: ColocationNode,
  enterpriseOnPrem: EnterpriseOnPremNode,
  nearEdge: NearEdgeNode,
  farEdge: FarEdgeNode,
  functionalEdge: FunctionalEdgeNode,
};

export const edgeTypes = {
  animatedData: AnimatedDataEdge,
  particle: ParticleEdge,
  disconnected: DisconnectedEdge,
};
```

---

## 3. Component Architecture

### 3.1 Core Flow Canvas

```typescript
// src/components/flow/FlowCanvas.tsx

import { ReactFlow, Background, Controls, MiniMap } from '@xyflow/react';
import { nodeTypes, edgeTypes } from '@/types/flow';

interface FlowCanvasProps {
  nodes: LocationNode[];
  edges: DataEdge[];
  onNodeClick: (nodeId: string) => void;
  animationConfig: AnimationConfig;
  isInteractive: boolean;
}

export function FlowCanvas({
  nodes,
  edges,
  onNodeClick,
  animationConfig,
  isInteractive
}: FlowCanvasProps) {
  return (
    <ReactFlow
      nodes={nodes}
      edges={edges}
      nodeTypes={nodeTypes}
      edgeTypes={edgeTypes}
      onNodeClick={(_, node) => onNodeClick(node.id)}
      fitView
      panOnDrag={isInteractive}
      zoomOnScroll={isInteractive}
      nodesDraggable={false}
    >
      <Background variant="dots" gap={20} size={1} />
      <Controls showInteractive={false} />
      <MiniMap nodeStrokeWidth={3} />
    </ReactFlow>
  );
}
```

### 3.2 Custom Node Component Pattern

```typescript
// src/components/flow/nodes/LocationNode.tsx

import { Handle, Position, NodeProps } from '@xyflow/react';
import { motion } from 'framer-motion';
import { cn } from '@/utils/cn';
import { PulsingGlow } from '@/components/animations/PulsingGlow';
import { LocationNodeData } from '@/types/flow';

export function LocationNode({ data, selected }: NodeProps<LocationNodeData>) {
  const { locationType, components, isActive, highlightType, onSelect } = data;
  
  return (
    <motion.div
      initial={{ scale: 0, opacity: 0 }}
      animate={{ scale: 1, opacity: 1 }}
      whileHover={{ scale: 1.05 }}
      transition={{ type: 'spring', stiffness: 300, damping: 20 }}
      onClick={() => onSelect(data.locationType.id)}
      className={cn(
        "relative p-4 rounded-xl border-2 cursor-pointer",
        "min-w-[140px] min-h-[100px]",
        "bg-gradient-to-br from-slate-800 to-slate-900",
        isActive && "border-emerald-500",
        !isActive && "border-slate-600 opacity-50",
        highlightType === 'positive' && "border-amber-400 shadow-amber-400/20",
        highlightType === 'negative' && "border-red-500 shadow-red-500/20",
        selected && "ring-2 ring-blue-500"
      )}
    >
      {/* Pulsing glow background for active nodes */}
      {isActive && <PulsingGlow color={locationType.color} />}
      
      {/* Node icon */}
      <div className="flex items-center justify-center mb-2">
        <span className="text-3xl">{getLocationIcon(locationType.icon)}</span>
      </div>
      
      {/* Node label */}
      <div className="text-center">
        <div className="text-sm font-semibold text-white">
          {locationType.shortName}
        </div>
        <div className="text-xs text-slate-400">
          {locationType.ownership}
        </div>
      </div>
      
      {/* Component count indicator */}
      {components.length > 0 && (
        <div className="absolute -top-2 -right-2 bg-blue-500 text-white text-xs px-2 py-1 rounded-full">
          {components.length}
        </div>
      )}
      
      {/* Connection handles */}
      <Handle type="source" position={Position.Right} className="w-3 h-3" />
      <Handle type="target" position={Position.Left} className="w-3 h-3" />
      <Handle type="source" position={Position.Bottom} id="bottom" className="w-3 h-3" />
      <Handle type="target" position={Position.Top} id="top" className="w-3 h-3" />
    </motion.div>
  );
}
```

### 3.3 Animated Edge Component

```typescript
// src/components/flow/edges/AnimatedDataEdge.tsx

import { BaseEdge, getBezierPath, EdgeProps } from '@xyflow/react';
import { DataEdgeData } from '@/types/flow';

const PARTICLE_COLORS = {
  data: '#3B82F6',      // Blue for data flow
  control: '#8B5CF6',   // Purple for control signals
  model: '#F59E0B',     // Amber for model transfers
  none: '#6B7280',      // Gray for inactive
};

export function AnimatedDataEdge({
  id,
  sourceX,
  sourceY,
  targetX,
  targetY,
  sourcePosition,
  targetPosition,
  data,
}: EdgeProps<DataEdgeData>) {
  const [edgePath] = getBezierPath({
    sourceX,
    sourceY,
    targetX,
    targetY,
    sourcePosition,
    targetPosition,
  });

  const particleColor = PARTICLE_COLORS[data?.dataFlowType || 'none'];

  return (
    <>
      {/* Base edge path */}
      <BaseEdge 
        id={id} 
        path={edgePath}
        style={{
          stroke: particleColor,
          strokeWidth: 2,
          opacity: data?.isAnimated ? 1 : 0.3,
        }}
      />
      
      {/* Animated particles */}
      {data?.isAnimated && (
        <>
          {/* Multiple particles with staggered timing for flow effect */}
          {[0, 0.33, 0.66].map((delay, i) => (
            <circle 
              key={i} 
              r="5" 
              fill={particleColor}
              filter="url(#glow)"
            >
              <animateMotion
                dur="3s"
                repeatCount="indefinite"
                path={edgePath}
                begin={`${delay * 3}s`}
              />
            </circle>
          ))}
          
          {/* SVG filter for glow effect */}
          <defs>
            <filter id="glow" x="-50%" y="-50%" width="200%" height="200%">
              <feGaussianBlur stdDeviation="3" result="blur" />
              <feMerge>
                <feMergeNode in="blur" />
                <feMergeNode in="SourceGraphic" />
              </feMerge>
            </filter>
          </defs>
        </>
      )}
    </>
  );
}
```

### 3.4 Scene Composition Example

```typescript
// src/components/scenes/HybridScene.tsx

import { useState } from 'react';
import { AnimatePresence, motion } from 'framer-motion';
import { FlowCanvas } from '@/components/flow/FlowCanvas';
import { NodeDetailPanel } from '@/components/panels/NodeDetailPanel';
import { Legend } from '@/components/ui/Legend';
import { hybridSceneConfig } from '@/data/scenes/hybrid';

export function HybridScene() {
  const [selectedNodeId, setSelectedNodeId] = useState<string | null>(null);
  
  const selectedNode = selectedNodeId 
    ? hybridSceneConfig.nodes.find(n => n.id === selectedNodeId)
    : null;
  
  return (
    <div className="relative w-full h-screen bg-slate-950">
      {/* Scene header */}
      <motion.div
        initial={{ y: -20, opacity: 0 }}
        animate={{ y: 0, opacity: 1 }}
        className="absolute top-6 left-6 z-10"
      >
        <h1 className="text-3xl font-bold text-white">
          {hybridSceneConfig.title}
        </h1>
        <p className="text-lg text-slate-400 mt-2">
          {hybridSceneConfig.subtitle}
        </p>
      </motion.div>
      
      {/* Key message banner */}
      <motion.div
        initial={{ opacity: 0 }}
        animate={{ opacity: 1 }}
        transition={{ delay: 0.5 }}
        className="absolute bottom-24 left-1/2 -translate-x-1/2 z-10"
      >
        <div className="bg-slate-800/80 backdrop-blur px-6 py-3 rounded-lg border border-slate-700">
          <p className="text-emerald-400 font-medium">
            {hybridSceneConfig.keyMessage}
          </p>
        </div>
      </motion.div>
      
      {/* Main flow visualization */}
      <FlowCanvas
        nodes={hybridSceneConfig.nodes}
        edges={hybridSceneConfig.edges}
        onNodeClick={setSelectedNodeId}
        animationConfig={hybridSceneConfig.animationConfig}
        isInteractive={true}
      />
      
      {/* Detail panel (slides in when node selected) */}
      <AnimatePresence>
        {selectedNode && (
          <NodeDetailPanel 
            node={selectedNode}
            onClose={() => setSelectedNodeId(null)}
          />
        )}
      </AnimatePresence>
      
      {/* Legend */}
      <Legend 
        items={[
          { color: '#F59E0B', label: 'Must be local (high value)' },
          { color: '#3B82F6', label: 'Can be offloaded (reduce complexity)' },
          { color: '#10B981', label: 'Active connection' },
        ]}
        className="absolute bottom-6 right-6"
      />
    </div>
  );
}
```

---

## 4. Scene Implementation Details

### 4.1 Scene 1: Traditional World

**Visual Concept:**
- 4 isolated "island" groups, one per deployment pattern
- Each island is a contained cluster with internal edges only
- NO connecting edges between islands
- Nodes appear static, minimal animation
- Gray/muted color palette indicating stagnation

**Layout Diagram:**
```
+------------------------------------------------------------------+
|                      TRADITIONAL WORLD                            |
|                                                                   |
|    +----------------+              +----------------+             |
|    |  BUY SaaS      |              |  BUY SaaS      |             |
|    |  (Fully Hosted)|              | (Fully On-Prem)|             |
|    |                |              |                |             |
|    |  [SaaS Vendor] |              | [Enterprise    |             |
|    |     DC         |              |    On-Prem]    |             |
|    +----------------+              +----------------+             |
|                                                                   |
|    +----------------+              +----------------+             |
|    |  BUILD         |              |  BUILD         |             |
|    | (Fully Cloud)  |              |(Fully On-Prem) |             |
|    |                |              |                |             |
|    | [Public Cloud] |              | [Enterprise    |             |
|    |                |              |    On-Prem]    |             |
|    +----------------+              +----------------+             |
|                                                                   |
|             "Siloed. Isolated. Limited."                          |
+------------------------------------------------------------------+
```

**Interactions:**
- Click on any island to see what components live there
- Hover reveals "This pattern has NO connection to other deployments"
- Visual barriers/walls between islands

### 4.2 Scene 2: Hybrid Reality (The Vision)

**Visual Concept:**
- All 10+ location types visible as nodes in a network topology
- Rich animated edges showing data/model/control flows
- Particles flowing continuously along ALL edges (the "living" effect)
- Pulsing glow on active nodes
- Color-coded by component constraint (must-be-local = gold, can-offload = blue)

**Layout Diagram:**
```
+------------------------------------------------------------------+
|                       HYBRID REALITY                              |
|                                                                   |
|       [Public Cloud]<---->[VPC]<---->[Neo Cloud]                 |
|             |               |              |                      |
|             v               v              v                      |
|       [SaaS Vendor]   [Colocation]   [On-Prem Cloud]             |
|             |               |              |                      |
|             +-------+-------+-------+------+                      |
|                     |               |                             |
|                     v               v                             |
|            [Near Edge]     [Enterprise]     [Near Edge]          |
|            (Cloud)          On-Prem        (Enterprise)          |
|                     |               |                             |
|                     +-------+-------+                             |
|                             |                                     |
|                     +-------+-------+                             |
|                     |               |                             |
|              [Far Edge]       [Functional Edge]                   |
|                                                                   |
|    "Interoperability enables efficiency. Everything connects.     |
|     High-value stays local, complexity offloads to cloud."        |
+------------------------------------------------------------------+
```

**Animations:**
- Continuous particle flow on all edges
- Particles color-coded by data type (blue=data, purple=control, amber=model)
- Nodes pulse when "processing"
- Smooth zoom/pan to focus on areas
- "Data highway" effect on major routes (more particles)

**Interactions:**
- Click any node to see hosted components with constraint indicators
- Filter by component type (e.g., "show only LLM locations")
- Toggle Buy vs Build perspective
- Highlight "must-be-local" vs "can-offload" components

### 4.3 Scene 3: Isolated On-Prem (Anti-Pattern)

**Visual Concept:**
- Enterprise on-prem node CENTER and LARGE
- All other nodes visible but GRAYED OUT
- NO edges connecting to other locations
- Warning indicators showing consequences
- Red/orange color scheme for danger/warning

**Layout Diagram:**
```
+------------------------------------------------------------------+
|             ISOLATED ON-PREM (Anti-Pattern)                       |
|                                                                   |
|      [Public Cloud]      [VPC]      [Neo Cloud]                  |
|          (gray)         (gray)        (gray)                     |
|             X              X            X                        |
|                                                                   |
|     [SaaS Vendor]     [Colocation]    [On-Prem Cloud]            |
|         (gray)          (gray)          (gray)                   |
|             X              X            X                        |
|                                                                   |
|              +-------------------------------+                    |
|              |                               |                    |
|              |    ENTERPRISE ON-PREM         |                    |
|              |    +---------------------+    |                    |
|              |    | LLMs           [!]  |    |                    |
|              |    | Data           [!]  |    |                    |
|              |    | Dev Tools      [!]  |    |                    |
|              |    | MLOps          [!]  |    |                    |
|              |    | Monitoring     [!]  |    |                    |
|              |    +---------------------+    |                    |
|              |                               |                    |
|              +-------------------------------+                    |
|                                                                   |
|  CONSEQUENCES:                                                    |
|  [!] Duplicated tooling (each team builds their own)             |
|  [!] Complexity explosion (no offloading)                        |
|  [!] Cannot scale beyond hardware limits                         |
|  [!] Developer friction (no cloud tools)                         |
|  [!] Slower innovation (manual everything)                       |
+------------------------------------------------------------------+
```

**Animations:**
- Broken/disconnected edge animations (dashed, flickering)
- Warning pulse on the isolated node
- "Chains" or barriers visualized around the island
- Comparison toggle to Scene 2 (split-screen option)

---

## 5. Animation Strategy

### 5.1 "Living, Breathing" Effect Components

| Effect | Implementation | Purpose |
|--------|---------------|---------|
| **Particle Flow** | SVG `<animateMotion>` along edge paths | Show data movement between locations |
| **Node Pulse** | Framer Motion `animate` with `repeat: Infinity` | Indicate active/processing nodes |
| **Glow Effect** | CSS `box-shadow` with animated opacity | Draw attention to key nodes |
| **Edge Shimmer** | SVG gradient animation along stroke | Show connection vitality |
| **Enter/Exit** | Framer Motion `AnimatePresence` | Smooth scene transitions |
| **Hover States** | Framer Motion `whileHover` | Interactive feedback |

### 5.2 Animation Hooks

```typescript
// src/hooks/useParticleSystem.ts

import { useState, useEffect } from 'react';
import { DataEdge, AnimationConfig } from '@/types';

interface Particle {
  id: string;
  edgeId: string;
  progress: number;  // 0-1 along path
  color: string;
}

export function useParticleSystem(edges: DataEdge[], config: AnimationConfig) {
  const [particles, setParticles] = useState<Particle[]>([]);
  
  useEffect(() => {
    if (!config.enableParticles) return;
    
    // Check for reduced motion preference
    const prefersReducedMotion = window.matchMedia(
      '(prefers-reduced-motion: reduce)'
    ).matches;
    
    if (prefersReducedMotion) return;
    
    let frameId: number;
    let lastTime = performance.now();
    
    const animate = (currentTime: number) => {
      const deltaTime = (currentTime - lastTime) / 1000;
      lastTime = currentTime;
      
      setParticles(prev => {
        // Update existing particle positions
        const updated = prev.map(p => ({
          ...p,
          progress: p.progress + (config.particleSpeed * deltaTime),
        })).filter(p => p.progress < 1);
        
        // Spawn new particles based on density
        const newParticles = edges
          .filter(e => e.data?.isAnimated)
          .flatMap(edge => {
            if (Math.random() < config.particleDensity * deltaTime) {
              return [{
                id: `${edge.id}-${Date.now()}`,
                edgeId: edge.id,
                progress: 0,
                color: getEdgeColor(edge.data?.dataFlowType),
              }];
            }
            return [];
          });
        
        return [...updated, ...newParticles];
      });
      
      frameId = requestAnimationFrame(animate);
    };
    
    frameId = requestAnimationFrame(animate);
    return () => cancelAnimationFrame(frameId);
  }, [edges, config]);
  
  return particles;
}
```

### 5.3 Scene Transitions

```typescript
// src/hooks/useSceneTransition.ts

import { useState, useCallback } from 'react';
import { useRouter } from 'next/navigation';
import { SceneId } from '@/types';

export function useSceneTransition() {
  const router = useRouter();
  const [currentScene, setCurrentScene] = useState<SceneId>('traditional');
  const [isTransitioning, setIsTransitioning] = useState(false);
  
  const transitionTo = useCallback(async (targetScene: SceneId) => {
    if (isTransitioning || targetScene === currentScene) return;
    
    setIsTransitioning(true);
    
    // 1. Fade out current scene (300ms)
    await new Promise(r => setTimeout(r, 300));
    
    // 2. Update scene state
    setCurrentScene(targetScene);
    
    // 3. Update URL
    router.push(`/${targetScene}`);
    
    // 4. Fade in new scene (300ms)
    await new Promise(r => setTimeout(r, 300));
    
    setIsTransitioning(false);
  }, [currentScene, isTransitioning, router]);
  
  return { currentScene, transitionTo, isTransitioning };
}
```

---

## 6. Navigation & Routing

### 6.1 URL Structure

```
/                     # Landing - scene selector or default to narrative
/traditional          # Scene 1: Traditional World
/hybrid               # Scene 2: Hybrid Reality
/isolated             # Scene 3: Isolated Anti-Pattern
/explorer             # Interactive Explorer Mode
/explorer?filter=llm  # Explorer with active filter
```

### 6.2 Navigation Component

```typescript
// src/components/navigation/SceneNavigator.tsx

import { motion } from 'framer-motion';
import { useSceneTransition } from '@/hooks/useSceneTransition';

const SCENE_ORDER: SceneId[] = ['traditional', 'hybrid', 'isolated'];

const SCENE_LABELS: Record<SceneId, string> = {
  traditional: 'Traditional World',
  hybrid: 'Hybrid Reality',
  isolated: 'Isolated Anti-Pattern',
  explorer: 'Explorer',
};

export function SceneNavigator() {
  const { currentScene, transitionTo, isTransitioning } = useSceneTransition();
  const [mode, setMode] = useState<'narrative' | 'explorer'>('narrative');
  
  const currentIndex = SCENE_ORDER.indexOf(currentScene);
  const hasPrevious = currentIndex > 0;
  const hasNext = currentIndex < SCENE_ORDER.length - 1;
  
  return (
    <nav className="fixed bottom-6 left-1/2 -translate-x-1/2 z-50">
      <motion.div 
        initial={{ y: 20, opacity: 0 }}
        animate={{ y: 0, opacity: 1 }}
        className="flex items-center gap-4 bg-slate-800/90 backdrop-blur px-6 py-3 rounded-full border border-slate-700"
      >
        {mode === 'narrative' ? (
          <>
            <button
              onClick={() => transitionTo(SCENE_ORDER[currentIndex - 1])}
              disabled={!hasPrevious || isTransitioning}
              className="px-4 py-2 rounded-lg bg-slate-700 hover:bg-slate-600 disabled:opacity-50"
            >
              Previous
            </button>
            
            {/* Progress dots */}
            <div className="flex gap-2">
              {SCENE_ORDER.map((scene, i) => (
                <div
                  key={scene}
                  className={cn(
                    "w-2 h-2 rounded-full transition-colors",
                    i === currentIndex ? "bg-emerald-500" : "bg-slate-600"
                  )}
                />
              ))}
            </div>
            
            <button
              onClick={() => transitionTo(SCENE_ORDER[currentIndex + 1])}
              disabled={!hasNext || isTransitioning}
              className="px-4 py-2 rounded-lg bg-emerald-600 hover:bg-emerald-500 disabled:opacity-50"
            >
              Next
            </button>
          </>
        ) : (
          <div className="flex gap-2">
            {SCENE_ORDER.map(scene => (
              <button
                key={scene}
                onClick={() => transitionTo(scene)}
                className={cn(
                  "px-4 py-2 rounded-lg transition-colors",
                  scene === currentScene 
                    ? "bg-emerald-600" 
                    : "bg-slate-700 hover:bg-slate-600"
                )}
              >
                {SCENE_LABELS[scene]}
              </button>
            ))}
          </div>
        )}
        
        {/* Mode toggle */}
        <div className="border-l border-slate-600 pl-4 ml-2">
          <button
            onClick={() => setMode(m => m === 'narrative' ? 'explorer' : 'narrative')}
            className="text-sm text-slate-400 hover:text-white"
          >
            {mode === 'narrative' ? 'Switch to Explorer' : 'Switch to Story'}
          </button>
        </div>
      </motion.div>
    </nav>
  );
}
```

---

## 7. Implementation Order (Build Sequence)

### Phase 1: Foundation (Days 1-2)
1. **Project Setup**
   - Initialize Next.js 14 with App Router
   - Install dependencies: `@xyflow/react`, `framer-motion`, `tailwindcss`, `zustand`, `lucide-react`
   - Configure TypeScript, Tailwind
   - Set up project folder structure

2. **Type Definitions**
   - Create `/src/types/location.ts`
   - Create `/src/types/component.ts`
   - Create `/src/types/scene.ts`
   - Create `/src/types/flow.ts`

3. **Basic Flow Canvas**
   - Implement basic FlowCanvas wrapper
   - Create simple LocationNode component
   - Test with hardcoded nodes to verify React Flow works

### Phase 2: Core Components (Days 3-4)
4. **Custom Nodes**
   - Implement LocationNode with all visual states
   - Add Framer Motion entry animations
   - Create PulsingGlow animation component
   - Style with Tailwind (dark theme)

5. **Custom Edges**
   - Implement AnimatedDataEdge with particles
   - Create SVG glow filter
   - Test particle animation performance

6. **Detail Panel**
   - Create NodeDetailPanel slide-in component
   - Create ComponentList for showing hosted components
   - Add constraint badges (must-be-local vs can-offload)

### Phase 3: Scenes (Days 5-7)
7. **Scene 1: Traditional World**
   - Define scene data in `/src/data/scenes/traditional.ts`
   - Implement TraditionalScene component
   - Create isolated island layout (4 groups)
   - Add pattern labels and descriptions

8. **Scene 2: Hybrid Reality**
   - Define comprehensive scene data in `/src/data/scenes/hybrid.ts`
   - Implement HybridScene component
   - Add all 10+ location nodes with positions
   - Configure all animated edges
   - Implement full particle system

9. **Scene 3: Isolated Anti-Pattern**
   - Define scene data in `/src/data/scenes/isolated.ts`
   - Implement IsolatedScene component
   - Create ConsequencePanel component
   - Add warning visuals and grayed-out nodes

### Phase 4: Interactivity (Days 8-9)
10. **Explorer Mode**
    - Implement ExplorerScene combining all nodes
    - Add FilterControls (by component type, location type)
    - Implement Buy vs Build perspective toggle
    - Add highlight modes for constraints

11. **Navigation & Transitions**
    - Implement SceneNavigator component
    - Create useSceneTransition hook
    - Add scene transition animations
    - Configure Next.js App Router pages

### Phase 5: Polish (Days 10-11)
12. **Animations & Effects**
    - Fine-tune particle speeds and densities
    - Implement glow intensity variations
    - Add hover state transitions
    - Test reduced-motion preference support

13. **Responsive & Accessibility**
    - Add mobile layout adjustments
    - Implement keyboard navigation for nodes
    - Add aria-labels and screen reader support
    - Test touch interactions

### Phase 6: Deployment (Day 12)
14. **Build & Deploy**
    - Run production build, fix any issues
    - Configure Vercel/Netlify deployment
    - Set up environment variables if needed
    - Test all features in production
    - Create README documentation

---

## 8. Key Technical Decisions

### 8.1 Why React Flow
- Industry standard for node-based UIs in React
- Excellent built-in zoom/pan controls
- Custom node/edge support is straightforward
- Active maintenance (xyflow team)
- Good TypeScript support

### 8.2 Why Framer Motion (not CSS animations)
- Declarative animation API integrates well with React
- AnimatePresence enables exit animations
- Variants system for coordinated animations
- Better control over animation lifecycle
- Gesture support (whileHover, whileTap)

### 8.3 Why Next.js App Router (not Vite)
- Clean URL structure with file-based routing
- Easy Vercel deployment (one-click)
- Built-in image optimization
- React Server Components for performance
- Better SEO if needed for public demos

### 8.4 State Management: Zustand
- Lightweight compared to Redux
- No boilerplate/providers needed
- Works well with React Flow
- Easy to add persistence (localStorage) if needed

---

## 9. Core Messages Mapping to Visuals

| Core Message | Scene | Visual Implementation |
|--------------|-------|----------------------|
| **Efficiency through offloading** | Hybrid | Show dev tools, MLOps, monitoring in cloud nodes with "reduces complexity" badge |
| **Interoperability is essential** | Hybrid | All nodes connected with continuous flowing particles |
| **Security is NOT one-size-fits-all** | Explorer | Filter reveals different constraints per industry/regulation |
| **Consequences of isolation** | Isolated | Warning badges, grayed disconnected nodes, consequence list |
| **High value stays local** | Hybrid | Gold/amber highlight on "must-be-local" components (LLMs, data) |
| **Complexity can be offloaded** | Hybrid | Blue highlight on "can-offload" components in cloud nodes |

---

## 10. Sample Data Files

### 10.1 Location Definitions

```typescript
// src/data/locations.ts

import { LocationType, LOCATION_TYPES } from '@/types/location';

export const locations: Record<string, LocationType> = {
  [LOCATION_TYPES.PUBLIC_CLOUD]: {
    id: 'public-cloud',
    name: 'Public Cloud Data Centers',
    shortName: 'Public Cloud',
    category: 'cloud',
    ownership: 'cloud-owned',
    description: 'Hyperscaler infrastructure (AWS, Azure, GCP)',
    icon: 'cloud',
    color: '#3B82F6',
    canHostLLMs: true,
    canHostSensitiveData: false,
    typicalLatency: 'medium',
    examples: ['AWS us-east-1', 'Azure West US', 'GCP us-central1'],
  },
  [LOCATION_TYPES.VPC]: {
    id: 'virtual-private-cloud',
    name: 'Virtual Private Cloud',
    shortName: 'VPC',
    category: 'cloud',
    ownership: 'enterprise-owned',
    description: 'Isolated cloud network controlled by enterprise',
    icon: 'cloud-lock',
    color: '#8B5CF6',
    canHostLLMs: true,
    canHostSensitiveData: true,
    typicalLatency: 'medium',
    examples: ['AWS VPC', 'Azure VNet', 'GCP VPC'],
  },
  [LOCATION_TYPES.ENTERPRISE_ON_PREM]: {
    id: 'enterprise-on-prem',
    name: 'Enterprise On-Premises Data Center',
    shortName: 'On-Prem DC',
    category: 'enterprise',
    ownership: 'enterprise-owned',
    description: 'Customer-owned and operated data center',
    icon: 'building-2',
    color: '#F59E0B',
    canHostLLMs: true,
    canHostSensitiveData: true,
    typicalLatency: 'low',
    examples: ['Corporate HQ DC', 'Regional Processing Center'],
  },
  [LOCATION_TYPES.FUNCTIONAL_EDGE]: {
    id: 'functional-edge',
    name: 'Functional Edge Devices',
    shortName: 'Devices',
    category: 'edge',
    ownership: 'enterprise-owned',
    description: 'End-user devices (phones, PCs, tablets)',
    icon: 'smartphone',
    color: '#10B981',
    canHostLLMs: true,  // SLMs
    canHostSensitiveData: true,
    typicalLatency: 'ultra-low',
    examples: ['Employee laptops', 'Mobile devices', 'Kiosks'],
  },
  // ... additional location types
};
```

### 10.2 Hybrid Scene Data

```typescript
// src/data/scenes/hybrid.ts

import { SceneConfig } from '@/types/scene';
import { LOCATION_TYPES } from '@/types/location';
import { COMPONENTS } from '@/types/component';

export const hybridSceneConfig: SceneConfig = {
  id: 'hybrid',
  title: 'The Hybrid Reality',
  subtitle: 'Everything connects',
  description: 'Modern AI infrastructure distributes components across locations based on value, compliance, and operational efficiency.',
  keyMessage: 'High-value stays local. Complexity offloads to cloud.',
  
  nodes: [
    // Cloud tier
    {
      id: 'public-cloud-1',
      locationType: LOCATION_TYPES.PUBLIC_CLOUD,
      position: { x: 400, y: 50 },
      components: [COMPONENTS.DEV_TOOLS.id, COMPONENTS.MLOPS.id, COMPONENTS.MONITORING.id],
      isActive: true,
    },
    {
      id: 'vpc-1',
      locationType: LOCATION_TYPES.VPC,
      position: { x: 600, y: 50 },
      components: [COMPONENTS.LLM.id],
      isActive: true,
    },
    {
      id: 'neo-cloud-1',
      locationType: LOCATION_TYPES.NEO_CLOUD,
      position: { x: 800, y: 50 },
      components: [COMPONENTS.MLOPS.id],
      isActive: true,
    },
    
    // Middle tier
    {
      id: 'saas-vendor-1',
      locationType: LOCATION_TYPES.SAAS_VENDOR,
      position: { x: 250, y: 200 },
      components: [COMPONENTS.MONITORING.id],
      isActive: true,
    },
    {
      id: 'colocation-1',
      locationType: LOCATION_TYPES.COLOCATION,
      position: { x: 500, y: 200 },
      components: [COMPONENTS.STORAGE_FILES.id],
      isActive: true,
    },
    {
      id: 'on-prem-cloud-1',
      locationType: LOCATION_TYPES.ON_PREM_CLOUD_OWNED,
      position: { x: 750, y: 200 },
      components: [COMPONENTS.LLM.id, COMPONENTS.SENSITIVE_DATA.id],
      isActive: true,
      highlight: 'positive',
    },
    
    // Enterprise tier
    {
      id: 'enterprise-onprem-1',
      locationType: LOCATION_TYPES.ENTERPRISE_ON_PREM,
      position: { x: 500, y: 350 },
      components: [COMPONENTS.LLM.id, COMPONENTS.SENSITIVE_DATA.id, COMPONENTS.STORAGE_FILES.id],
      isActive: true,
      highlight: 'positive',
    },
    
    // Edge tier
    {
      id: 'near-edge-1',
      locationType: LOCATION_TYPES.NEAR_EDGE_ENTERPRISE,
      position: { x: 300, y: 500 },
      components: [COMPONENTS.SLM.id],
      isActive: true,
    },
    {
      id: 'far-edge-1',
      locationType: LOCATION_TYPES.FAR_EDGE_ENTERPRISE,
      position: { x: 500, y: 500 },
      components: [COMPONENTS.SLM.id],
      isActive: true,
    },
    {
      id: 'functional-edge-1',
      locationType: LOCATION_TYPES.FUNCTIONAL_EDGE,
      position: { x: 700, y: 500 },
      components: [COMPONENTS.SLM.id],
      isActive: true,
    },
  ],
  
  edges: [
    // Cloud tier connections
    { id: 'e1', source: 'public-cloud-1', target: 'vpc-1', animated: true, dataFlowType: 'control', bidirectional: true },
    { id: 'e2', source: 'vpc-1', target: 'neo-cloud-1', animated: true, dataFlowType: 'model', bidirectional: false },
    
    // Cloud to middle tier
    { id: 'e3', source: 'public-cloud-1', target: 'saas-vendor-1', animated: true, dataFlowType: 'data', bidirectional: true },
    { id: 'e4', source: 'public-cloud-1', target: 'colocation-1', animated: true, dataFlowType: 'data', bidirectional: true },
    { id: 'e5', source: 'vpc-1', target: 'on-prem-cloud-1', animated: true, dataFlowType: 'model', bidirectional: true },
    
    // Middle tier to enterprise
    { id: 'e6', source: 'colocation-1', target: 'enterprise-onprem-1', animated: true, dataFlowType: 'data', bidirectional: true },
    { id: 'e7', source: 'on-prem-cloud-1', target: 'enterprise-onprem-1', animated: true, dataFlowType: 'control', bidirectional: true },
    
    // Enterprise to edge
    { id: 'e8', source: 'enterprise-onprem-1', target: 'near-edge-1', animated: true, dataFlowType: 'model', bidirectional: false },
    { id: 'e9', source: 'enterprise-onprem-1', target: 'far-edge-1', animated: true, dataFlowType: 'model', bidirectional: false },
    { id: 'e10', source: 'enterprise-onprem-1', target: 'functional-edge-1', animated: true, dataFlowType: 'model', bidirectional: false },
    
    // Cross-connections
    { id: 'e11', source: 'saas-vendor-1', target: 'enterprise-onprem-1', animated: true, dataFlowType: 'control', bidirectional: true },
    { id: 'e12', source: 'neo-cloud-1', target: 'colocation-1', animated: true, dataFlowType: 'data', bidirectional: true },
  ],
  
  animationConfig: {
    particleSpeed: 0.3,
    particleDensity: 0.5,
    pulseInterval: 2000,
    enableParticles: true,
    enableGlow: true,
  },
};
```

---

## 11. Dependencies (package.json)

```json
{
  "name": "hybrid-ai-viz",
  "version": "1.0.0",
  "private": true,
  "scripts": {
    "dev": "next dev",
    "build": "next build",
    "start": "next start",
    "lint": "next lint"
  },
  "dependencies": {
    "@xyflow/react": "^12.0.0",
    "framer-motion": "^11.0.0",
    "lucide-react": "^0.300.0",
    "next": "^14.0.0",
    "react": "^18.2.0",
    "react-dom": "^18.2.0",
    "zustand": "^4.4.0",
    "clsx": "^2.0.0",
    "tailwind-merge": "^2.0.0"
  },
  "devDependencies": {
    "@types/node": "^20.0.0",
    "@types/react": "^18.2.0",
    "@types/react-dom": "^18.2.0",
    "autoprefixer": "^10.0.0",
    "eslint": "^8.0.0",
    "eslint-config-next": "^14.0.0",
    "postcss": "^8.0.0",
    "tailwindcss": "^3.4.0",
    "typescript": "^5.0.0"
  }
}
```

---

## Critical Files for Implementation

1. **`/src/types/location.ts`** - Core type definitions for all location types; foundation for the entire data model

2. **`/src/components/flow/FlowCanvas.tsx`** - Main React Flow wrapper; all scenes depend on this component working correctly

3. **`/src/components/flow/edges/AnimatedDataEdge.tsx`** - The "living, breathing" effect depends on this edge animation implementation with SVG particles

4. **`/src/data/scenes/hybrid.ts`** - The most complex scene definition with all nodes/edges; serves as template for other scenes

5. **`/src/hooks/useSceneTransition.ts`** - Controls navigation and transitions between all scenes; critical for user experience and routing
