import PptxGenJS from 'pptxgenjs'
import type { SlideContent } from '../slideContent'

// McKinsey/BCG color palette
const colors = {
  primary: '005eb8',
  secondary: '222222',
  lightGray: 'f5f5f5',
  mediumGray: 'a2aaad',
  accent: '0a3d62',
  success: '2d8a5e',
  error: 'c0392b',
  text: '333333',
  textLight: '666666',
  white: 'ffffff',
}

const fonts = {
  heading: 'Georgia',
  body: 'Arial',
}

interface PptxOptions {
  author?: string
  title?: string
  subject?: string
}

export function exportToPptx(slides: SlideContent[], options: PptxOptions = {}): void {
  const pptx = new PptxGenJS()
  
  pptx.author = options.author || 'Corporate Strategy'
  pptx.title = options.title || 'Strategy, Goals & Tactics'
  pptx.subject = options.subject || 'Corporate Strategy Framework'
  
  pptx.defineLayout({ name: 'WIDESCREEN', width: 10, height: 5.625 })
  pptx.layout = 'WIDESCREEN'
  
  // Slide 1 - Definitions
  const slide1 = pptx.addSlide()
  renderDefinitionsSlide(slide1, slides[0])
  
  // Slide 2 - Alignment
  const slide2 = pptx.addSlide()
  renderAlignmentSlide(slide2, slides[1])
  
  pptx.writeFile({ fileName: 'Strategy-Goals-Tactics.pptx' })
}

function renderDefinitionsSlide(slide: PptxGenJS.Slide, content: SlideContent): void {
  const sections = content.sections || []
  
  // Title
  slide.addText(content.title, { 
    x: 0.5, y: 0.25, w: 9, h: 0.4, 
    fontSize: 22, fontFace: fonts.heading, bold: true, 
    color: colors.secondary, align: 'center' 
  })
  
  if (content.subtitle) {
    slide.addText(content.subtitle, { 
      x: 0.5, y: 0.65, w: 9, h: 0.25, 
      fontSize: 12, fontFace: fonts.body, 
      color: colors.textLight, align: 'center' 
    })
  }
  
  // Three columns
  const colW = 2.95
  const colGap = 0.1
  const startY = 0.95
  
  sections.forEach((section, idx) => {
    const x = 0.5 + idx * (colW + colGap)
    
    // Left border accent
    slide.addShape('rect', { x, y: startY, w: 0.03, h: 3.4, fill: { color: colors.primary } })
    
    // Label badge
    slide.addText(section.heading, { 
      x: x + 0.08, y: startY, w: 1.1, h: 0.28, 
      fontSize: 11, fontFace: fonts.body, bold: true, 
      color: colors.white, fill: { color: colors.primary }, 
      align: 'center', valign: 'middle' 
    })
    
    // Subheading
    slide.addText(section.subheading || '', { 
      x: x + 0.08, y: startY + 0.32, w: colW - 0.1, h: 0.18, 
      fontSize: 9, fontFace: fonts.body, color: colors.textLight, italic: true 
    })
    
    // Definition box
    slide.addShape('rect', { 
      x: x + 0.08, y: startY + 0.52, w: colW - 0.1, h: 0.55, 
      fill: { color: colors.lightGray } 
    })
    slide.addText(section.definition || '', { 
      x: x + 0.12, y: startY + 0.55, w: colW - 0.18, h: 0.48, 
      fontSize: 8, fontFace: fonts.body, color: colors.text, valign: 'top' 
    })
    
    // Key components
    if (section.components) {
      slide.addText('KEY COMPONENTS', { 
        x: x + 0.08, y: startY + 1.12, w: colW - 0.1, h: 0.15, 
        fontSize: 7, fontFace: fonts.body, bold: true, color: colors.primary 
      })
      
      const compText = section.components.slice(0, 3).map(c => {
        const short = c.split(':')[0]
        return { text: `• ${short}`, options: { bullet: false } }
      })
      slide.addText(compText, { 
        x: x + 0.08, y: startY + 1.28, w: colW - 0.1, h: 0.55, 
        fontSize: 7, fontFace: fonts.body, color: colors.text, valign: 'top' 
      })
    }
    
    // Correct example
    if (section.examples?.correct?.[0]) {
      slide.addText('✓ CORRECT', { 
        x: x + 0.08, y: startY + 1.88, w: colW - 0.1, h: 0.15, 
        fontSize: 7, fontFace: fonts.body, bold: true, color: colors.success 
      })
      slide.addShape('rect', { 
        x: x + 0.08, y: startY + 2.03, w: colW - 0.1, h: 0.55, 
        fill: { color: 'f0fdf4' } 
      })
      slide.addText(section.examples.correct[0].text, { 
        x: x + 0.12, y: startY + 2.06, w: colW - 0.18, h: 0.48, 
        fontSize: 7, fontFace: fonts.body, color: colors.text, italic: true, valign: 'top' 
      })
    }
    
    // Incorrect example
    if (section.examples?.incorrect?.[0]) {
      slide.addText('✗ INCORRECT', { 
        x: x + 0.08, y: startY + 2.63, w: colW - 0.1, h: 0.15, 
        fontSize: 7, fontFace: fonts.body, bold: true, color: colors.error 
      })
      slide.addShape('rect', { 
        x: x + 0.08, y: startY + 2.78, w: colW - 0.1, h: 0.55, 
        fill: { color: 'fef2f2' } 
      })
      slide.addText(section.examples.incorrect[0].text, { 
        x: x + 0.12, y: startY + 2.81, w: colW - 0.18, h: 0.28, 
        fontSize: 7, fontFace: fonts.body, color: colors.text, italic: true, valign: 'top' 
      })
      if (section.examples.incorrect[0].note) {
        slide.addText(`↳ ${section.examples.incorrect[0].note}`, { 
          x: x + 0.12, y: startY + 3.08, w: colW - 0.18, h: 0.22, 
          fontSize: 6, fontFace: fonts.body, color: colors.textLight, valign: 'top' 
        })
      }
    }
  })
  
  // Key insight bar
  if (content.keyInsight) {
    slide.addShape('rect', { x: 0, y: 4.45, w: 10, h: 0.35, fill: { color: colors.secondary } })
    slide.addText(content.keyInsight, { 
      x: 0.5, y: 4.5, w: 9, h: 0.25, 
      fontSize: 10, fontFace: fonts.body, color: colors.white, align: 'center', valign: 'middle' 
    })
  }
  
  // Footer with sources
  const sourceText = content.sources?.map(s => s.text).join(' | ') || ''
  slide.addText(sourceText, { 
    x: 0.5, y: 4.9, w: 8, h: 0.4, 
    fontSize: 7, fontFace: fonts.body, color: colors.textLight, valign: 'top' 
  })
  slide.addText('1 / 2', { 
    x: 8.8, y: 5.3, w: 0.7, h: 0.2, 
    fontSize: 10, fontFace: fonts.body, color: colors.textLight, align: 'right' 
  })
}

function renderAlignmentSlide(slide: PptxGenJS.Slide, content: SlideContent): void {
  // Title
  slide.addText(content.title, { 
    x: 0.5, y: 0.25, w: 9, h: 0.4, 
    fontSize: 20, fontFace: fonts.heading, bold: true, 
    color: colors.secondary, align: 'center' 
  })
  
  const panelW = 4.4
  const panelH = 3.3
  const panelY = 0.75
  
  // ===== WITHOUT STRATEGY PANEL =====
  const x1 = 0.5
  
  // Panel background
  slide.addShape('rect', { x: x1, y: panelY, w: panelW, h: panelH, fill: { color: 'fef2f2' } })
  slide.addShape('rect', { x: x1, y: panelY, w: panelW, h: 0.04, fill: { color: colors.error } })
  
  // Header
  slide.addText('✗ WITHOUT STRATEGY', { 
    x: x1 + 0.1, y: panelY + 0.1, w: panelW - 0.2, h: 0.25, 
    fontSize: 12, fontFace: fonts.body, bold: true, color: colors.error 
  })
  slide.addText('No guardrails → scattered effort, wasted resources', { 
    x: x1 + 0.1, y: panelY + 0.35, w: panelW - 0.2, h: 0.18, 
    fontSize: 9, fontFace: fonts.body, color: colors.textLight, italic: true 
  })
  
  // Empty strategy box
  slide.addShape('rect', { 
    x: x1 + 0.15, y: panelY + 0.58, w: panelW - 0.3, h: 0.35, 
    fill: { color: 'e5e7eb' }, line: { color: '9ca3af', pt: 1, dashType: 'dash' } 
  })
  slide.addText('No Strategy Defined', { 
    x: x1 + 0.15, y: panelY + 0.58, w: panelW - 0.3, h: 0.35, 
    fontSize: 10, fontFace: fonts.body, color: colors.textLight, align: 'center', valign: 'middle' 
  })
  
  // Goal
  slide.addShape('rect', { 
    x: x1 + 0.15, y: panelY + 0.98, w: panelW - 0.3, h: 0.3, 
    fill: { color: colors.accent } 
  })
  slide.addText('🎯 GOAL: Grow Revenue', { 
    x: x1 + 0.15, y: panelY + 0.98, w: panelW - 0.3, h: 0.3, 
    fontSize: 10, fontFace: fonts.body, bold: true, color: colors.white, align: 'center', valign: 'middle' 
  })
  
  // NO GUARDRAILS zone - open area with scattered people
  slide.addShape('rect', { 
    x: x1 + 0.15, y: panelY + 1.33, w: panelW - 0.3, h: 1.1, 
    fill: { color: 'fecaca' }, transparency: 70 
  })
  
  // Scattered people going different directions
  const scatteredPositions = [
    { x: x1 + 0.3, y: panelY + 1.4, text: '↖ Employee A', rot: -10 },
    { x: x1 + 2.4, y: panelY + 1.4, text: 'Employee B ↗', rot: 10 },
    { x: x1 + 0.3, y: panelY + 1.8, text: '↙ Employee C', rot: 5 },
    { x: x1 + 2.4, y: panelY + 1.8, text: 'Employee D ↘', rot: -5 },
  ]
  scatteredPositions.forEach(p => {
    slide.addShape('rect', { 
      x: p.x, y: p.y, w: 1.7, h: 0.28, 
      fill: { color: colors.white }, line: { color: colors.error, pt: 1 }, rotate: p.rot 
    })
    slide.addText(p.text, { 
      x: p.x, y: p.y, w: 1.7, h: 0.28, 
      fontSize: 8, fontFace: fonts.body, bold: true, color: colors.error, 
      align: 'center', valign: 'middle', rotate: p.rot 
    })
  })
  
  // Scattered tactics
  const scatteredTactics = [
    { x: x1 + 0.25, y: panelY + 2.15, text: '"Cut costs"', rot: -4 },
    { x: x1 + 2.2, y: panelY + 2.15, text: '"Enterprise"', rot: 3 },
    { x: x1 + 0.25, y: panelY + 2.48, text: '"Global"', rot: 5 },
    { x: x1 + 2.2, y: panelY + 2.48, text: '"Discount"', rot: -3 },
  ]
  scatteredTactics.forEach(t => {
    slide.addShape('rect', { 
      x: t.x, y: t.y, w: 1.85, h: 0.28, 
      fill: { color: colors.white }, line: { color: colors.error, pt: 1 }, rotate: t.rot 
    })
    slide.addText(t.text, { 
      x: t.x, y: t.y, w: 1.85, h: 0.28, 
      fontSize: 8, fontFace: fonts.body, color: colors.text, 
      align: 'center', valign: 'middle', rotate: t.rot 
    })
  })
  
  // Result
  slide.addShape('rect', { 
    x: x1 + 0.15, y: panelY + 2.85, w: panelW - 0.3, h: 0.35, 
    fill: { color: colors.error } 
  })
  slide.addText('RESULT: Conflicting priorities, organizational drift', { 
    x: x1 + 0.15, y: panelY + 2.85, w: panelW - 0.3, h: 0.35, 
    fontSize: 9, fontFace: fonts.body, bold: true, color: colors.white, 
    align: 'center', valign: 'middle' 
  })
  
  // ===== WITH STRATEGY PANEL =====
  const x2 = 5.1
  
  // Panel background
  slide.addShape('rect', { x: x2, y: panelY, w: panelW, h: panelH, fill: { color: 'f0fdf4' } })
  slide.addShape('rect', { x: x2, y: panelY, w: panelW, h: 0.04, fill: { color: colors.success } })
  
  // Header
  slide.addText('✓ WITH STRATEGY', { 
    x: x2 + 0.1, y: panelY + 0.1, w: panelW - 0.2, h: 0.25, 
    fontSize: 12, fontFace: fonts.body, bold: true, color: colors.success 
  })
  slide.addText('Clear guardrails → aligned execution, compounding advantage', { 
    x: x2 + 0.1, y: panelY + 0.35, w: panelW - 0.2, h: 0.18, 
    fontSize: 9, fontFace: fonts.body, color: colors.textLight, italic: true 
  })
  
  // Strategy box
  slide.addShape('rect', { 
    x: x2 + 0.15, y: panelY + 0.58, w: panelW - 0.3, h: 0.45, 
    fill: { color: colors.primary } 
  })
  slide.addText('STRATEGY: Win mid-market manufacturing', { 
    x: x2 + 0.15, y: panelY + 0.58, w: panelW - 0.3, h: 0.28, 
    fontSize: 10, fontFace: fonts.body, bold: true, color: colors.white, 
    align: 'center', valign: 'middle' 
  })
  slide.addText('Trade-off: NOT enterprise, NOT horizontal', { 
    x: x2 + 0.15, y: panelY + 0.82, w: panelW - 0.3, h: 0.18, 
    fontSize: 8, fontFace: fonts.body, color: 'ffffff', transparency: 20, 
    align: 'center', valign: 'middle' 
  })
  
  // Goal
  slide.addShape('rect', { 
    x: x2 + 0.15, y: panelY + 1.08, w: panelW - 0.3, h: 0.3, 
    fill: { color: colors.accent } 
  })
  slide.addText('🎯 GOAL: 500 Mfg Customers by 2026', { 
    x: x2 + 0.15, y: panelY + 1.08, w: panelW - 0.3, h: 0.3, 
    fontSize: 10, fontFace: fonts.body, bold: true, color: colors.white, 
    align: 'center', valign: 'middle' 
  })
  
  // GUARDRAILS zone with visible rails
  // Left guardrail
  slide.addShape('rect', { 
    x: x2 + 0.15, y: panelY + 1.43, w: 0.3, h: 1.0, 
    fill: { color: colors.success } 
  })
  slide.addText('G\nU\nA\nR\nD\nR\nA\nI\nL', { 
    x: x2 + 0.15, y: panelY + 1.48, w: 0.3, h: 0.9, 
    fontSize: 5, fontFace: fonts.body, bold: true, color: colors.white, 
    align: 'center', valign: 'middle' 
  })
  
  // Right guardrail
  slide.addShape('rect', { 
    x: x2 + panelW - 0.45, y: panelY + 1.43, w: 0.3, h: 1.0, 
    fill: { color: colors.success } 
  })
  slide.addText('G\nU\nA\nR\nD\nR\nA\nI\nL', { 
    x: x2 + panelW - 0.45, y: panelY + 1.48, w: 0.3, h: 0.9, 
    fontSize: 5, fontFace: fonts.body, bold: true, color: colors.white, 
    align: 'center', valign: 'middle' 
  })
  
  // Middle zone
  slide.addShape('rect', { 
    x: x2 + 0.5, y: panelY + 1.43, w: panelW - 1.0, h: 1.0, 
    fill: { color: 'bbf7d0' }, transparency: 50 
  })
  
  // Aligned people all pointing down
  const alignedPeople = [
    { y: panelY + 1.48, text: '↓ Employee A' },
    { y: panelY + 1.73, text: '↓ Employee B' },
    { y: panelY + 1.98, text: '↓ Employee C' },
    { y: panelY + 2.23, text: '↓ Employee D' },
  ]
  alignedPeople.forEach(p => {
    slide.addShape('rect', { 
      x: x2 + 0.6, y: p.y, w: panelW - 1.2, h: 0.22, 
      fill: { color: colors.white }, line: { color: colors.success, pt: 1 } 
    })
    slide.addText(p.text, { 
      x: x2 + 0.6, y: p.y, w: panelW - 1.2, h: 0.22, 
      fontSize: 8, fontFace: fonts.body, bold: true, color: colors.success, 
      align: 'center', valign: 'middle' 
    })
  })
  
  // Aligned tactics
  const alignedTactics = [
    { x: x2 + 0.2, y: panelY + 2.5, text: 'NAM sponsor' },
    { x: x2 + 2.15, y: panelY + 2.5, text: 'Vertical reps' },
    { x: x2 + 0.2, y: panelY + 2.75, text: 'Mfg LinkedIn' },
    { x: x2 + 2.15, y: panelY + 2.75, text: 'Case studies' },
  ]
  alignedTactics.forEach(t => {
    slide.addShape('rect', { 
      x: t.x, y: t.y, w: 1.95, h: 0.22, 
      fill: { color: colors.white }, line: { color: colors.success, pt: 1 } 
    })
    slide.addText(t.text, { 
      x: t.x, y: t.y, w: 1.95, h: 0.22, 
      fontSize: 8, fontFace: fonts.body, color: colors.text, 
      align: 'center', valign: 'middle' 
    })
  })
  
  // Result
  slide.addShape('rect', { 
    x: x2 + 0.15, y: panelY + 3.02, w: panelW - 0.3, h: 0.22, 
    fill: { color: colors.success } 
  })
  slide.addText('RESULT: Reinforcing tactics, compounding advantage', { 
    x: x2 + 0.15, y: panelY + 3.02, w: panelW - 0.3, h: 0.22, 
    fontSize: 9, fontFace: fonts.body, bold: true, color: colors.white, 
    align: 'center', valign: 'middle' 
  })
  
  // Key insight bar
  if (content.keyInsight) {
    slide.addShape('rect', { x: 0, y: 4.15, w: 10, h: 0.6, fill: { color: colors.secondary } })
    slide.addText(content.keyInsight, { 
      x: 0.5, y: 4.2, w: 9, h: 0.5, 
      fontSize: 10, fontFace: fonts.body, color: colors.white, 
      align: 'center', valign: 'middle' 
    })
  }
  
  // Footer with sources
  const sourceText = content.sources?.map(s => s.text).join(' | ') || ''
  slide.addText(sourceText, { 
    x: 0.5, y: 4.85, w: 8, h: 0.5, 
    fontSize: 7, fontFace: fonts.body, color: colors.textLight, valign: 'top' 
  })
  slide.addText('2 / 2', { 
    x: 8.8, y: 5.3, w: 0.7, h: 0.2, 
    fontSize: 10, fontFace: fonts.body, color: colors.textLight, align: 'right' 
  })
}
