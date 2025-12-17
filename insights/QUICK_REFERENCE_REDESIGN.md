# Quick Reference: PowerPoint Redesign Guide

## At a Glance

| Metric | Current State | Target State | Change |
|--------|---------------|--------------|--------|
| **Slides** | 2 | 2 | No change |
| **Avg Shapes/Slide** | 59 | 25 | -58% reduction |
| **Slides with Titles** | 0 | 2 | Add titles |
| **Primary Font** | Arial | Calibri | Upgrade |
| **Color Strategy** | Minimal | Full palette | Enhancement |

---

## Slide 1: Strategy vs. Goals vs. Tactics

### Current Layout
```
┌─────────────────────────────────────────────┐
│  STRATEGY  │   GOALS    │   TACTICS         │
│  49 shapes • Text-heavy • No color          │
└─────────────────────────────────────────────┘
```

### Redesigned Layout
```
┌─────────────────────────────────────────────┐
│ [TITLE] Strategy vs. Goals vs. Tactics      │
│ [SUBTITLE] Understanding the hierarchy...   │
│                                             │
│ ┌───────┐   ┌───────┐   ┌───────┐         │
│ │   🎯  │   │   📊  │   │   ⚙️  │         │
│ │STRATGY│   │ GOALS │   │TACTICS│         │
│ │       │   │       │   │       │         │
│ │ [Def] │   │ [Def] │   │ [Def] │         │
│ │       │   │       │   │       │         │
│ │✓ Ex   │   │✓ Ex   │   │✓ Ex   │         │
│ │✗ Ex   │   │✗ Ex   │   │✗ Ex   │         │
│ └───────┘   └───────┘   └───────┘         │
│                                             │
│ Key insight: Strategy defines what NOT...   │
└─────────────────────────────────────────────┘
```

**Key Changes:**
- Add title and subtitle
- Icons for each column header
- Colored backgrounds for example boxes (green for ✓, red for ✗)
- Reduce from 49 to ~22 shapes
- Increase white space by 40%

---

## Slide 2: Strategy Creates Alignment

### Current Layout
```
┌─────────────────────────────────────────────┐
│  WITHOUT STRATEGY  │  WITH STRATEGY         │
│  69 shapes • Complex flow • 4 images        │
└─────────────────────────────────────────────┘
```

### Redesigned Layout
```
┌─────────────────────────────────────────────┐
│ [TITLE] Strategy Creates Alignment—...      │
│                                             │
│ ✗ WITHOUT          │  ✓ WITH               │
│ ┌──────────┐      │  ┌──────────┐         │
│ │No Strategy│      │  │ STRATEGY │         │
│ └──────────┘      │  │Trade-offs│         │
│      ↓            │  └──────────┘         │
│    GOAL           │      ↓                 │
│      ↓            │  ╔══════════╗         │
│  ↙ ↘ ↖ ↗         │  ║  GOAL    ║         │
│ Scattered         │  ╚══════════╝         │
│  tactics          │      ↓                 │
│      ↓            │    ║ ║ ║ ║            │
│   [Result]        │   Aligned              │
│                   │      ↓                 │
│                   │   [Result]             │
├───────────────────┴─────────────────────────┤
│ "The essence of strategy is choosing..."    │
└─────────────────────────────────────────────┘
```

**Key Changes:**
- Add clear title
- Visual guardrails (║ symbols) around aligned side
- Stronger arrow visualization
- Color-coded: Red tones (left) vs. Green/Blue tones (right)
- Reduce from 69 to ~28 shapes
- Prominent Porter quote footer

---

## Color Palette

### Primary Colors
| Color | Hex | Usage |
|-------|-----|-------|
| Strategy Blue | `#2E5090` | Strategy column, headers |
| Goals Teal | `#008B8B` | Goals column, goal boxes |
| Tactics Blue | `#4A6FA5` | Tactics column |

### Semantic Colors
| Color | Hex | Usage |
|-------|-----|-------|
| Correct Green | `#2D7A3E` | ✓ examples, WITH STRATEGY side |
| Incorrect Red | `#C4342D` | ✗ examples, WITHOUT STRATEGY side |
| Neutral Gray | `#5A5A5A` | Body text, descriptors |

### Backgrounds
| Color | Hex | Usage |
|-------|-----|-------|
| Light Blue-Gray | `#F5F7FA` | Column backgrounds |
| White | `#FFFFFF` | Main slide background |
| Pale Blue | `#E8F0F8` | Accent backgrounds |

---

## Typography Scale

| Element | Font | Size | Weight | Color |
|---------|------|------|--------|-------|
| **Title** | Calibri | 32pt | Bold | #2E5090 |
| **Subtitle** | Calibri | 18pt | Italic | #5A5A5A |
| **Header** | Calibri | 24pt | Bold | #2E5090 |
| **Descriptor** | Calibri | 14pt | Italic | #5A5A5A |
| **Body** | Calibri | 12pt | Regular | #2D2D2D |
| **Example** | Calibri | 11pt | Italic | #2D2D2D |
| **Footer** | Calibri | 10pt | Italic | #5A5A5A |

---

## Content Preservation Checklist

### Slide 1: Must Preserve
- [x] Three-column structure (Strategy, Goals, Tactics)
- [x] All three definitions (exact wording)
- [x] Descriptor text ("Where & how to compete", etc.)
- [x] All 6 examples (3 correct ✓, 3 incorrect ✗)
- [x] All 3 explanations for incorrect examples
- [x] Key insight footer (exact wording)
- [x] SMART framework reference in Goals definition

### Slide 2: Must Preserve
- [x] Side-by-side comparison structure
- [x] WITHOUT STRATEGY vs. WITH STRATEGY labels
- [x] All 8 tactic examples (4 per side)
- [x] Both result statements
- [x] Porter quote (exact wording)
- [x] "Guardrails" terminology
- [x] Trade-off language in strategy box
- [x] Goal emojis (🎯)

---

## Critical Design Rules

### DO ✓
1. Use semantic colors (green = good, red = bad)
2. Create strong visual hierarchy through size
3. Add icons to reinforce concepts
4. Use white space generously (40% increase)
5. Make examples scannable (colored boxes)
6. Show flow with clear arrows (Slide 2)
7. Visualize "guardrails" literally (Slide 2)
8. Keep all original text content intact

### DON'T ✗
1. Change any definitions or example wording
2. Remove any content from original slides
3. Use more than 3 primary colors
4. Create slides with >30 shapes
5. Use font sizes smaller than 10pt
6. Rely solely on color to convey meaning
7. Make text boxes too narrow (<3" wide)
8. Overlap text with images/shapes

---

## Shape Budget per Slide

### Slide 1 Target: 22 shapes
- 3 column background rectangles
- 3 header icons
- 3 header texts
- 3 descriptor texts
- 3 definition text boxes
- 6 example boxes (with integrated ✓/✗)
- 1 key insight footer box

### Slide 2 Target: 28 shapes
- 2 section background rectangles
- 2 header texts
- 2 strategy boxes
- 2 goal boxes
- 8 tactic boxes (4 + 4)
- 2 result boxes
- 1 quote footer box
- 6 arrows/flow indicators
- 2 guardrail visual elements

---

## PptxGenJS Code Structure

### Slide 1 Implementation Pattern
```javascript
slide1.addText("Strategy vs. Goals vs. Tactics", {
  x: 0.5, y: 0.3, w: 9.0, h: 0.4,
  fontSize: 32, bold: true, color: "2E5090"
});

// Three columns (loop through)
const columns = [
  { x: 0.5, header: "STRATEGY", icon: "🎯", color: "2E5090" },
  { x: 3.5, header: "GOALS", icon: "📊", color: "008B8B" },
  { x: 6.5, header: "TACTICS", icon: "⚙️", color: "4A6FA5" }
];

columns.forEach(col => {
  // Background
  slide1.addShape(pptx.ShapeType.rect, {
    x: col.x, y: 0.9, w: 2.8, h: 4.0,
    fill: { color: "F5F7FA" }
  });

  // Header with icon
  slide1.addText(`${col.icon} ${col.header}`, {
    x: col.x, y: 1.0, w: 2.8, h: 0.4,
    fontSize: 24, bold: true, color: col.color
  });

  // Definition, examples, etc.
});
```

### Slide 2 Implementation Pattern
```javascript
// Side-by-side comparison
const sides = [
  {
    x: 0.5,
    label: "✗ WITHOUT STRATEGY",
    color: "C4342D",
    style: "chaos"
  },
  {
    x: 5.3,
    label: "✓ WITH STRATEGY",
    color: "2D7A3E",
    style: "aligned"
  }
];

sides.forEach(side => {
  // Background
  slide2.addShape(pptx.ShapeType.rect, {
    x: side.x, y: 0.9, w: 4.4, h: 4.2,
    fill: { color: side.style === "chaos" ? "FFEBEE" : "E8F5E9" }
  });

  // Flow arrows based on style
  if (side.style === "chaos") {
    // Add scattered arrows
  } else {
    // Add aligned arrows with guardrails
  }
});
```

---

## Testing Checklist

### Visual Quality
- [ ] All text is readable at standard viewing distance
- [ ] Colors have sufficient contrast (WCAG AA)
- [ ] No overlapping elements
- [ ] Consistent spacing throughout
- [ ] Professional appearance

### Content Accuracy
- [ ] All definitions match original verbatim
- [ ] All examples included (6 on Slide 1, 8 tactics on Slide 2)
- [ ] Porter quote exact
- [ ] No typos or formatting errors

### Executive Readiness
- [ ] Key message clear within 10 seconds
- [ ] Slides work without presenter narration
- [ ] Printable in grayscale (test!)
- [ ] Accessible to color-blind viewers
- [ ] Professional enough for C-suite presentation

### Technical
- [ ] Exports correctly to PDF
- [ ] File size reasonable (<5MB)
- [ ] No missing fonts when shared
- [ ] Compatible with PowerPoint and Keynote

---

## File Locations

### Analysis Files (Generated)
- `/Users/nicholaspate/Documents/01_Active/Corp_Strat/ezAI/insights/pptx_analysis_detailed.json`
- `/Users/nicholaspate/Documents/01_Active/Corp_Strat/ezAI/insights/pptx_analysis_report.md`
- `/Users/nicholaspate/Documents/01_Active/Corp_Strat/ezAI/insights/pptx_design_analysis.md`
- `/Users/nicholaspate/Documents/01_Active/Corp_Strat/ezAI/insights/pptx_recommendations.md`
- `/Users/nicholaspate/Documents/01_Active/Corp_Strat/ezAI/insights/COMPREHENSIVE_PPTX_ANALYSIS.md`

### Source File
- `/Users/nicholaspate/Documents/01_Active/Corp_Strat/ezAI/insights/strategy-goals-tactics-slides.pptx`

### Analysis Script
- `/Users/nicholaspate/Documents/01_Active/Corp_Strat/ezAI/analyze_pptx.py`

---

## Next Steps

1. **Review** this analysis with stakeholders
2. **Finalize** color palette (confirm corporate colors)
3. **Prototype** Slide 1 in PptxGenJS
4. **Get approval** on Slide 1 design
5. **Complete** Slide 2 implementation
6. **Test** with executive audience
7. **Iterate** based on feedback
8. **Deliver** final presentation

---

**Pro Tip:** Start with Slide 1 as it's simpler (22 shapes vs. 28). Perfect the column layout pattern, then apply learnings to Slide 2's comparison layout.

