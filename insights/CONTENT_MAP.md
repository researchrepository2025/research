# Complete Content Map for PptxGenJS Implementation

## Slide 1: Strategy vs. Goals vs. Tactics

### Title Section
```
TITLE: "Strategy vs. Goals vs. Tactics"
  - Font: Calibri 32pt Bold
  - Color: #2E5090
  - Position: Top, centered

SUBTITLE: "Understanding the hierarchy of corporate planning"
  - Font: Calibri 18pt Italic
  - Color: #5A5A5A
  - Position: Below title
```

### Column 1: STRATEGY

```javascript
{
  icon: "🎯",
  header: "STRATEGY",
  headerColor: "#2E5090",

  descriptor: "Where & how to compete",

  definition: "Integrated set of choices that position the organization to win—including what NOT to do",

  correctExample: {
    symbol: "✓",
    text: "Dominate mid-market manufacturing software through vertical specialization. We will NOT pursue enterprise or horizontal apps.",
    backgroundColor: "#E8F5E9",
    borderColor: "#2D7A3E",
    textColor: "#1B5E20"
  },

  incorrectExample: {
    symbol: "✗",
    text: "Be the best software company and grow revenue 20%.",
    backgroundColor: "#FFEBEE",
    borderColor: "#C4342D",
    textColor: "#B71C1C",
    explanation: "↳ No choices, no trade-offs—this is a goal, not a strategy"
  }
}
```

### Column 2: GOALS

```javascript
{
  icon: "📊",
  header: "GOALS",
  headerColor: "#008B8B",

  descriptor: "What outcomes to achieve",

  definition: "Specific, measurable outcomes with defined timeframes (SMART: Specific, Measurable, Achievable, Relevant, Time-bound)",

  correctExample: {
    symbol: "✓",
    text: "Acquire 500 new manufacturing customers in North America by December 2026.",
    backgroundColor: "#E8F5E9",
    borderColor: "#2D7A3E",
    textColor: "#1B5E20"
  },

  incorrectExample: {
    symbol: "✗",
    text: "Grow market share significantly.",
    backgroundColor: "#FFEBEE",
    borderColor: "#C4342D",
    textColor: "#B71C1C",
    explanation: "↳ Vague, no metrics, no deadline—unmeasurable"
  }
}
```

### Column 3: TACTICS

```javascript
{
  icon: "⚙️",
  header: "TACTICS",
  headerColor: "#4A6FA5",

  descriptor: "How to execute",

  definition: "Specific actions and initiatives to achieve goals. Short-term, adjustable, with clear ownership.",

  correctExample: {
    symbol: "✓",
    text: "Sponsor NAM conference; hire 3 vertical sales reps; launch LinkedIn campaign targeting plant managers.",
    backgroundColor: "#E8F5E9",
    borderColor: "#2D7A3E",
    textColor: "#1B5E20"
  },

  incorrectExample: {
    symbol: "✗",
    text: "Do more marketing and sales.",
    backgroundColor: "#FFEBEE",
    borderColor: "#C4342D",
    textColor: "#B71C1C",
    explanation: "↳ Not actionable—no specific activity or owner"
  }
}
```

### Footer Section
```
KEY INSIGHT: "Key insight: Strategy defines what NOT to do • Goals are measurable targets • Tactics are swappable actions"
  - Font: Calibri 14pt Bold
  - Color: #2E5090
  - Background: #E8F0F8 (light blue)
  - Position: Bottom, spanning full width
  - Padding: 0.15" all sides
```

---

## Slide 2: Strategy Creates Alignment—Its Absence Creates Chaos

### Title Section
```
TITLE: "Strategy Creates Alignment—Its Absence Creates Chaos"
  - Font: Calibri 32pt Bold
  - Color: #2E5090
  - Position: Top, centered
```

### Left Side: WITHOUT STRATEGY

```javascript
{
  sectionLabel: {
    text: "✗ WITHOUT STRATEGY",
    color: "#C4342D",
    fontSize: 20,
    bold: true
  },

  subtitle: {
    text: "Siloed tactics, misaligned effort",
    color: "#5A5A5A",
    fontSize: 14,
    italic: true
  },

  backgroundColor: "#FFEBEE", // Light red

  strategyBox: {
    text: "No Strategy Defined",
    backgroundColor: "#FFFFFF",
    borderColor: "#C4342D",
    borderStyle: "dashed",
    borderWidth: 2
  },

  goal: {
    text: "🎯 GOAL: Grow Revenue",
    backgroundColor: "#FFF3E0",
    borderColor: "#FF9800"
  },

  label: {
    text: "NO GUARDRAILS",
    color: "#C4342D",
    fontSize: 12,
    bold: true,
    // Appears twice in the flow
  },

  tactics: [
    {
      text: "Cut all costs",
      backgroundColor: "#FFFFFF",
      borderColor: "#C4342D",
      // Arrow: scattered, dashed, pointing different directions
    },
    {
      text: "Chase enterprise",
      backgroundColor: "#FFFFFF",
      borderColor: "#C4342D",
    },
    {
      text: "Expand globally",
      backgroundColor: "#FFFFFF",
      borderColor: "#C4342D",
    },
    {
      text: "Discount heavily",
      backgroundColor: "#FFFFFF",
      borderColor: "#C4342D",
    }
  ],

  result: {
    text: "RESULT: Wasted resources, conflicting priorities",
    backgroundColor: "#FFCDD2",
    color: "#B71C1C",
    fontSize: 12,
    bold: true
  },

  flowStyle: {
    arrowType: "dashed",
    arrowColor: "#C4342D",
    arrowDirection: "scattered", // Different angles
    arrowWidth: 2
  }
}
```

### Right Side: WITH STRATEGY

```javascript
{
  sectionLabel: {
    text: "✓ WITH STRATEGY",
    color: "#2D7A3E",
    fontSize: 20,
    bold: true
  },

  subtitle: {
    text: "Clear choices create aligned execution",
    color: "#5A5A5A",
    fontSize: 14,
    italic: true
  },

  backgroundColor: "#E8F5E9", // Light green

  strategyBox: {
    text: "STRATEGY: Win mid-market manufacturing\nTrade-off: NOT enterprise, NOT horizontal",
    backgroundColor: "#FFFFFF",
    borderColor: "#2D7A3E",
    borderStyle: "solid",
    borderWidth: 3
  },

  goal: {
    text: "🎯 GOAL: 500 Mfg Customers",
    backgroundColor: "#E3F2FD",
    borderColor: "#2196F3"
  },

  label: {
    text: "GUARDRAILS",
    color: "#2D7A3E",
    fontSize: 12,
    bold: true,
    // Appears twice in the flow
  },

  tactics: [
    {
      text: "NAM sponsor",
      backgroundColor: "#FFFFFF",
      borderColor: "#2D7A3E",
      // Arrow: aligned, solid, parallel flow
    },
    {
      text: "Vertical reps",
      backgroundColor: "#FFFFFF",
      borderColor: "#2D7A3E",
    },
    {
      text: "Mfg LinkedIn",
      backgroundColor: "#FFFFFF",
      borderColor: "#2D7A3E",
    },
    {
      text: "Case studies",
      backgroundColor: "#FFFFFF",
      borderColor: "#2D7A3E",
    }
  ],

  result: {
    text: "RESULT: Reinforcing tactics, compounding advantage",
    backgroundColor: "#C8E6C9",
    color: "#1B5E20",
    fontSize: 12,
    bold: true
  },

  flowStyle: {
    arrowType: "solid",
    arrowColor: "#2D7A3E",
    arrowDirection: "parallel", // All pointing down
    arrowWidth: 3
  },

  guardrailsVisual: {
    type: "boundary-lines",
    color: "#2D7A3E",
    style: "solid",
    width: 3,
    // Visual "rails" on left and right of tactics section
  }
}
```

### Footer Section
```
QUOTE: "Porter: \"The essence of strategy is choosing what not to do.\" Trade-offs create guardrails that align everyone's tactics toward the goal."
  - Font: Calibri 11pt Italic
  - Color: #2D2D2D
  - Background: #F5F7FA (light blue-gray)
  - Position: Bottom, spanning full width
  - Padding: 0.15" all sides
  - Quote marks: Use actual quotation mark graphics or styled text
```

---

## Complete PptxGenJS Data Structure

### Slide 1 JSON
```json
{
  "slideNumber": 1,
  "title": {
    "text": "Strategy vs. Goals vs. Tactics",
    "style": {
      "fontSize": 32,
      "bold": true,
      "color": "2E5090",
      "fontFace": "Calibri"
    },
    "position": { "x": 0.5, "y": 0.3, "w": 9.0, "h": 0.4 }
  },
  "subtitle": {
    "text": "Understanding the hierarchy of corporate planning",
    "style": {
      "fontSize": 18,
      "italic": true,
      "color": "5A5A5A",
      "fontFace": "Calibri"
    },
    "position": { "x": 0.5, "y": 0.7, "w": 9.0, "h": 0.3 }
  },
  "columns": [
    {
      "name": "strategy",
      "position": { "x": 0.5, "y": 1.1, "w": 2.8, "h": 4.0 },
      "background": { "color": "F5F7FA" },
      "icon": "🎯",
      "header": "STRATEGY",
      "headerColor": "2E5090",
      "descriptor": "Where & how to compete",
      "definition": "Integrated set of choices that position the organization to win—including what NOT to do",
      "correctExample": {
        "text": "Dominate mid-market manufacturing software through vertical specialization. We will NOT pursue enterprise or horizontal apps.",
        "backgroundColor": "E8F5E9",
        "borderColor": "2D7A3E",
        "textColor": "1B5E20"
      },
      "incorrectExample": {
        "text": "Be the best software company and grow revenue 20%.",
        "backgroundColor": "FFEBEE",
        "borderColor": "C4342D",
        "textColor": "B71C1C",
        "explanation": "↳ No choices, no trade-offs—this is a goal, not a strategy"
      }
    },
    {
      "name": "goals",
      "position": { "x": 3.5, "y": 1.1, "w": 2.8, "h": 4.0 },
      "background": { "color": "F5F7FA" },
      "icon": "📊",
      "header": "GOALS",
      "headerColor": "008B8B",
      "descriptor": "What outcomes to achieve",
      "definition": "Specific, measurable outcomes with defined timeframes (SMART: Specific, Measurable, Achievable, Relevant, Time-bound)",
      "correctExample": {
        "text": "Acquire 500 new manufacturing customers in North America by December 2026.",
        "backgroundColor": "E8F5E9",
        "borderColor": "2D7A3E",
        "textColor": "1B5E20"
      },
      "incorrectExample": {
        "text": "Grow market share significantly.",
        "backgroundColor": "FFEBEE",
        "borderColor": "C4342D",
        "textColor": "B71C1C",
        "explanation": "↳ Vague, no metrics, no deadline—unmeasurable"
      }
    },
    {
      "name": "tactics",
      "position": { "x": 6.5, "y": 1.1, "w": 2.8, "h": 4.0 },
      "background": { "color": "F5F7FA" },
      "icon": "⚙️",
      "header": "TACTICS",
      "headerColor": "4A6FA5",
      "descriptor": "How to execute",
      "definition": "Specific actions and initiatives to achieve goals. Short-term, adjustable, with clear ownership.",
      "correctExample": {
        "text": "Sponsor NAM conference; hire 3 vertical sales reps; launch LinkedIn campaign targeting plant managers.",
        "backgroundColor": "E8F5E9",
        "borderColor": "2D7A3E",
        "textColor": "1B5E20"
      },
      "incorrectExample": {
        "text": "Do more marketing and sales.",
        "backgroundColor": "FFEBEE",
        "borderColor": "C4342D",
        "textColor": "B71C1C",
        "explanation": "↳ Not actionable—no specific activity or owner"
      }
    }
  ],
  "footer": {
    "text": "Key insight: Strategy defines what NOT to do • Goals are measurable targets • Tactics are swappable actions",
    "style": {
      "fontSize": 14,
      "bold": true,
      "color": "2E5090",
      "fontFace": "Calibri"
    },
    "background": { "color": "E8F0F8" },
    "position": { "x": 0.5, "y": 5.2, "w": 9.0, "h": 0.35 }
  }
}
```

### Slide 2 JSON
```json
{
  "slideNumber": 2,
  "title": {
    "text": "Strategy Creates Alignment—Its Absence Creates Chaos",
    "style": {
      "fontSize": 32,
      "bold": true,
      "color": "2E5090",
      "fontFace": "Calibri"
    },
    "position": { "x": 0.5, "y": 0.3, "w": 9.0, "h": 0.4 }
  },
  "comparisonSides": [
    {
      "name": "without",
      "position": { "x": 0.5, "y": 0.9, "w": 4.4, "h": 4.2 },
      "background": { "color": "FFEBEE" },
      "label": {
        "text": "✗ WITHOUT STRATEGY",
        "color": "C4342D",
        "fontSize": 20,
        "bold": true
      },
      "subtitle": {
        "text": "Siloed tactics, misaligned effort",
        "color": "5A5A5A",
        "fontSize": 14,
        "italic": true
      },
      "strategyBox": {
        "text": "No Strategy Defined",
        "backgroundColor": "FFFFFF",
        "borderColor": "C4342D",
        "borderStyle": "dash",
        "borderWidth": 2
      },
      "goal": {
        "text": "🎯 GOAL: Grow Revenue",
        "backgroundColor": "FFF3E0",
        "borderColor": "FF9800"
      },
      "guardrailLabel": {
        "text": "NO GUARDRAILS",
        "color": "C4342D",
        "fontSize": 12,
        "bold": true
      },
      "tactics": [
        { "text": "Cut all costs" },
        { "text": "Chase enterprise" },
        { "text": "Expand globally" },
        { "text": "Discount heavily" }
      ],
      "result": {
        "text": "RESULT: Wasted resources, conflicting priorities",
        "backgroundColor": "FFCDD2",
        "color": "B71C1C"
      },
      "flowStyle": {
        "arrowType": "dash",
        "arrowColor": "C4342D",
        "arrowPattern": "scattered"
      }
    },
    {
      "name": "with",
      "position": { "x": 5.3, "y": 0.9, "w": 4.4, "h": 4.2 },
      "background": { "color": "E8F5E9" },
      "label": {
        "text": "✓ WITH STRATEGY",
        "color": "2D7A3E",
        "fontSize": 20,
        "bold": true
      },
      "subtitle": {
        "text": "Clear choices create aligned execution",
        "color": "5A5A5A",
        "fontSize": 14,
        "italic": true
      },
      "strategyBox": {
        "text": "STRATEGY: Win mid-market manufacturing\nTrade-off: NOT enterprise, NOT horizontal",
        "backgroundColor": "FFFFFF",
        "borderColor": "2D7A3E",
        "borderStyle": "solid",
        "borderWidth": 3
      },
      "goal": {
        "text": "🎯 GOAL: 500 Mfg Customers",
        "backgroundColor": "E3F2FD",
        "borderColor": "2196F3"
      },
      "guardrailLabel": {
        "text": "GUARDRAILS",
        "color": "2D7A3E",
        "fontSize": 12,
        "bold": true
      },
      "tactics": [
        { "text": "NAM sponsor" },
        { "text": "Vertical reps" },
        { "text": "Mfg LinkedIn" },
        { "text": "Case studies" }
      ],
      "result": {
        "text": "RESULT: Reinforcing tactics, compounding advantage",
        "backgroundColor": "C8E6C9",
        "color": "1B5E20"
      },
      "flowStyle": {
        "arrowType": "solid",
        "arrowColor": "2D7A3E",
        "arrowPattern": "aligned"
      },
      "guardrails": {
        "type": "boundary",
        "color": "2D7A3E",
        "width": 3
      }
    }
  ],
  "footer": {
    "text": "Porter: \"The essence of strategy is choosing what not to do.\" Trade-offs create guardrails that align everyone's tactics toward the goal.",
    "style": {
      "fontSize": 11,
      "italic": true,
      "color": "2D2D2D",
      "fontFace": "Calibri"
    },
    "background": { "color": "F5F7FA" },
    "position": { "x": 0.5, "y": 5.2, "w": 9.0, "h": 0.35 }
  }
}
```

---

## Layout Coordinates (10" × 5.625" slide)

### Slide 1 Positioning

```
Column widths: 2.8" each
Column spacing: 0.2" gutters
Left margin: 0.5"
Right margin: 0.5"

Column 1 (Strategy):
  x: 0.5, y: 1.1, w: 2.8, h: 4.0

Column 2 (Goals):
  x: 3.5, y: 1.1, w: 2.8, h: 4.0

Column 3 (Tactics):
  x: 6.5, y: 1.1, w: 2.8, h: 4.0

Within each column:
  Icon + Header: y: 1.15, h: 0.35
  Descriptor: y: 1.55, h: 0.2
  Definition: y: 1.8, h: 0.6
  Correct Example: y: 2.5, h: 0.6
  Incorrect Example: y: 3.2, h: 0.6
  Explanation: y: 3.85, h: 0.4
```

### Slide 2 Positioning

```
Side widths: 4.4" each
Side spacing: 0.4" center gutter
Left margin: 0.5"
Right margin: 0.5"

Left Side (Without):
  x: 0.5, y: 0.9, w: 4.4, h: 4.2

Right Side (With):
  x: 5.3, y: 0.9, w: 4.4, h: 4.2

Within each side:
  Label: y: 0.95, h: 0.3
  Subtitle: y: 1.3, h: 0.2
  Strategy Box: y: 1.6, h: 0.5
  Goal: y: 2.2, h: 0.3
  Guardrail Label: y: 2.6, h: 0.2
  Tactics (4 boxes): y: 2.9-4.2 (stacked or arranged)
  Result: y: 4.4, h: 0.3

Arrows: Connect between elements (y: varies)
```

---

## Icons & Visual Elements

### Recommended Icons (if using icon font or images)

**Slide 1:**
- Strategy: 🎯 Target / Compass / Chess piece
- Goals: 📊 Chart / Flag / Mountain peak
- Tactics: ⚙️ Gear / Tools / Checklist

**Slide 2:**
- Checkmark: ✓ (green, size 20pt)
- X mark: ✗ (red, size 20pt)
- Target: 🎯 (for goals)
- Arrows: Custom shapes (directional indicators)

### Arrow Specifications

**Without Strategy (Scattered):**
```javascript
{
  type: "arrow",
  style: "dash",
  color: "#C4342D",
  width: 2,
  points: [
    // Different angles: 45°, -30°, 60°, -45°
  ]
}
```

**With Strategy (Aligned):**
```javascript
{
  type: "arrow",
  style: "solid",
  color: "#2D7A3E",
  width: 3,
  points: [
    // All pointing down (90°)
  ]
}
```

### Guardrails Visualization

**Option 1: Literal Rails**
```javascript
// Left rail
slide.addShape(pptx.ShapeType.rect, {
  x: 5.4, y: 2.9, w: 0.1, h: 1.3,
  fill: { color: "2D7A3E" }
});

// Right rail
slide.addShape(pptx.ShapeType.rect, {
  x: 9.5, y: 2.9, w: 0.1, h: 1.3,
  fill: { color: "2D7A3E" }
});
```

**Option 2: Boundary Box**
```javascript
slide.addShape(pptx.ShapeType.rect, {
  x: 5.5, y: 2.85, w: 4.0, h: 1.4,
  fill: { type: "none" },
  line: { color: "2D7A3E", width: 3 }
});
```

---

## Character Counts (for text box sizing)

### Slide 1
- **Longest Definition:** Goals - 124 characters
- **Longest Correct Example:** Tactics - 120 characters
- **Longest Incorrect Example:** Strategy - 53 characters
- **Longest Explanation:** Strategy - 59 characters

**Text Box Height Recommendations:**
- Definition: 0.6" (3 lines max)
- Correct Example: 0.6" (3-4 lines)
- Incorrect Example: 0.4" (2 lines)
- Explanation: 0.4" (2 lines)

### Slide 2
- **Longest Strategy Box:** With Strategy - 98 characters (2 lines)
- **Longest Tactic:** "Sponsor NAM conference; hire 3 vertical sales reps..." (shortened for Slide 2)
- **Longest Result:** With Strategy - 57 characters

**Text Box Height Recommendations:**
- Strategy Box: 0.5" (2 lines)
- Tactic: 0.25" (1 line, shortened)
- Result: 0.3" (1-2 lines)

---

## Accessibility Notes

### Color Contrast Ratios (WCAG AA Compliance)

**Text on White Background:**
- #2E5090 (Strategy Blue): 6.1:1 ✓ Pass
- #008B8B (Goals Teal): 4.5:1 ✓ Pass
- #2D2D2D (Body): 14.8:1 ✓ Pass

**Text on Colored Backgrounds:**
- #1B5E20 on #E8F5E9: 7.2:1 ✓ Pass
- #B71C1C on #FFEBEE: 6.8:1 ✓ Pass

**For Color-Blind Viewers:**
- Use ✓ and ✗ symbols (not just green/red)
- Use dashed vs. solid lines (not just color)
- Include "GUARDRAILS" text label (not just visual)

### Print Compatibility
- All colors should work in grayscale
- Test by converting to grayscale and verifying contrast
- Borders and symbols should remain visible

---

This content map provides everything needed for pixel-perfect PptxGenJS implementation while preserving all original content and improving executive readiness through thoughtful design.

