import React from 'react'
import { SlideBase } from './SlideBase'
import { theme } from '../theme'
import type { SlideContent } from '../slideContent'

interface AlignmentSlideProps {
  content: SlideContent
  slideNumber: number
  totalSlides: number
}

export const AlignmentSlide: React.FC<AlignmentSlideProps> = ({ 
  content, 
  slideNumber, 
  totalSlides 
}) => {
  const footerText = content.sources?.map(s => s.text).join(' | ') || content.footer
  
  return (
    <SlideBase slideNumber={slideNumber} totalSlides={totalSlides} footer={footerText}>
      {/* Title */}
      <div style={styles.header}>
        <h1 style={styles.title}>{content.title}</h1>
      </div>
      
      {/* Two-panel comparison */}
      <div style={styles.panelsContainer}>
        {/* WITHOUT STRATEGY panel */}
        <div style={{...styles.panel, ...styles.panelLeft}}>
          <div style={styles.panelHeader}>
            <span style={styles.xIcon}>❌</span>
            <span style={styles.panelTitle}>WITHOUT STRATEGY</span>
          </div>
          <p style={styles.panelSubtitle}>No guardrails → scattered effort, wasted resources</p>
          
          <div style={styles.flowContainer}>
            {/* Empty strategy box */}
            <div style={styles.strategyBoxEmpty}>
              <span style={styles.questionIcon}>❓</span>
              <span>No Strategy Defined</span>
            </div>
            
            {/* Goal */}
            <div style={styles.goalBox}>
              <span style={styles.goalIcon}>🎯</span>
              <span>GOAL: Grow Revenue</span>
            </div>
            
            {/* NO GUARDRAILS - chaos zone */}
            <div style={styles.chaosZone}>
              <div style={styles.chaosLabel}>
                <span>🚫 NO GUARDRAILS 🚫</span>
              </div>
              
              {/* Scattered people with arrows going different directions */}
              <div style={styles.scatteredPeopleGrid}>
                <div style={{...styles.personScattered, transform: 'rotate(-25deg)'}}>
                  <span style={styles.personIcon}>👤</span>
                  <span style={styles.arrowScattered}>↖️</span>
                </div>
                <div style={{...styles.personScattered, transform: 'rotate(20deg)'}}>
                  <span style={styles.arrowScattered}>↗️</span>
                  <span style={styles.personIcon}>👤</span>
                </div>
                <div style={{...styles.personScattered, transform: 'rotate(15deg)'}}>
                  <span style={styles.personIcon}>👤</span>
                  <span style={styles.arrowScattered}>↙️</span>
                </div>
                <div style={{...styles.personScattered, transform: 'rotate(-20deg)'}}>
                  <span style={styles.arrowScattered}>↘️</span>
                  <span style={styles.personIcon}>👤</span>
                </div>
                <div style={{...styles.personScattered, transform: 'rotate(30deg)'}}>
                  <span style={styles.personIcon}>👤</span>
                  <span style={styles.arrowScattered}>⬅️</span>
                </div>
                <div style={{...styles.personScattered, transform: 'rotate(-15deg)'}}>
                  <span style={styles.arrowScattered}>➡️</span>
                  <span style={styles.personIcon}>👤</span>
                </div>
              </div>
              
              {/* Scattered tactics */}
              <div style={styles.scatteredTactics}>
                <div style={{...styles.tacticBad, transform: 'rotate(-8deg)'}}>"Cut costs" 📉</div>
                <div style={{...styles.tacticBad, transform: 'rotate(5deg)'}}>🏢 "Enterprise"</div>
                <div style={{...styles.tacticBad, transform: 'rotate(10deg)'}}>"Global" 🌍</div>
                <div style={{...styles.tacticBad, transform: 'rotate(-5deg)'}}>💰 "Discount"</div>
              </div>
            </div>
            
            {/* Result */}
            <div style={styles.resultBad}>
              <span style={styles.resultIcon}>💥</span>
              <span>RESULT: Conflicting priorities, organizational drift</span>
            </div>
          </div>
        </div>
        
        {/* WITH STRATEGY panel */}
        <div style={{...styles.panel, ...styles.panelRight}}>
          <div style={styles.panelHeaderGood}>
            <span style={styles.checkIcon}>✅</span>
            <span style={styles.panelTitle}>WITH STRATEGY</span>
          </div>
          <p style={styles.panelSubtitle}>Clear guardrails → aligned execution, compounding advantage</p>
          
          <div style={styles.flowContainer}>
            {/* Strategy box */}
            <div style={styles.strategyBoxFull}>
              <div style={styles.strategyRow}>
                <span style={styles.strategyIcon}>🎯</span>
                <span style={styles.strategyLabel}>STRATEGY: Win mid-market manufacturing</span>
              </div>
              <div style={styles.tradeoffRow}>
                <span style={styles.tradeoffIcon}>🚫</span>
                <span style={styles.tradeoffLabel}>Trade-off: NOT enterprise, NOT horizontal</span>
              </div>
            </div>
            
            {/* Goal */}
            <div style={styles.goalBoxGood}>
              <span style={styles.goalIcon}>🎯</span>
              <span>GOAL: 500 Mfg Customers by 2026</span>
            </div>
            
            {/* WITH GUARDRAILS - funnel zone */}
            <div style={styles.funnelZone}>
              {/* Left guardrail */}
              <div style={styles.guardrailLeft}>
                <div style={styles.guardrailInner}>
                  <span style={styles.guardrailIcon}>🛡️</span>
                  <span style={styles.guardrailText}>G<br/>U<br/>A<br/>R<br/>D<br/>R<br/>A<br/>I<br/>L</span>
                </div>
              </div>
              
              {/* Aligned people zone */}
              <div style={styles.alignedZone}>
                <div style={styles.alignedPeopleGrid}>
                  <div style={styles.personAligned}>
                    <span style={styles.personIcon}>👤</span>
                    <span style={styles.arrowDown}>⬇️</span>
                  </div>
                  <div style={styles.personAligned}>
                    <span style={styles.personIcon}>👤</span>
                    <span style={styles.arrowDown}>⬇️</span>
                  </div>
                  <div style={styles.personAligned}>
                    <span style={styles.personIcon}>👤</span>
                    <span style={styles.arrowDown}>⬇️</span>
                  </div>
                  <div style={styles.personAligned}>
                    <span style={styles.personIcon}>👤</span>
                    <span style={styles.arrowDown}>⬇️</span>
                  </div>
                  <div style={styles.personAligned}>
                    <span style={styles.personIcon}>👤</span>
                    <span style={styles.arrowDown}>⬇️</span>
                  </div>
                  <div style={styles.personAligned}>
                    <span style={styles.personIcon}>👤</span>
                    <span style={styles.arrowDown}>⬇️</span>
                  </div>
                </div>
              </div>
              
              {/* Right guardrail */}
              <div style={styles.guardrailRight}>
                <div style={styles.guardrailInner}>
                  <span style={styles.guardrailIcon}>🛡️</span>
                  <span style={styles.guardrailText}>G<br/>U<br/>A<br/>R<br/>D<br/>R<br/>A<br/>I<br/>L</span>
                </div>
              </div>
            </div>
            
            {/* Aligned tactics */}
            <div style={styles.alignedTactics}>
              <div style={styles.tacticGood}>🎪 NAM sponsor</div>
              <div style={styles.tacticGood}>👔 Vertical reps</div>
              <div style={styles.tacticGood}>💼 Mfg LinkedIn</div>
              <div style={styles.tacticGood}>📚 Case studies</div>
            </div>
            
            {/* Result */}
            <div style={styles.resultGood}>
              <span style={styles.resultIcon}>🚀</span>
              <span>RESULT: Reinforcing tactics, compounding advantage</span>
            </div>
          </div>
        </div>
      </div>
      
      {/* Key insight footer */}
      {content.keyInsight && (
        <div style={styles.keyInsightBar}>
          <span style={styles.quoteIcon}>💬</span>
          <p style={styles.keyInsightText}>{content.keyInsight}</p>
        </div>
      )}
    </SlideBase>
  )
}

const styles: Record<string, React.CSSProperties> = {
  header: {
    marginBottom: '8px',
  },
  title: {
    fontSize: '18px',
    fontWeight: 700,
    color: theme.colors.secondary,
    fontFamily: theme.typography.fontFamily.heading,
    margin: 0,
    textAlign: 'center',
  },
  panelsContainer: {
    display: 'flex',
    gap: '12px',
    flex: 1,
  },
  panel: {
    flex: 1,
    padding: '10px',
    borderRadius: '6px',
    display: 'flex',
    flexDirection: 'column',
  },
  panelLeft: {
    backgroundColor: '#fef2f2',
    border: `2px solid ${theme.colors.error}`,
  },
  panelRight: {
    backgroundColor: '#f0fdf4',
    border: `2px solid ${theme.colors.success}`,
  },
  panelHeader: {
    display: 'flex',
    alignItems: 'center',
    gap: '6px',
    color: theme.colors.error,
    marginBottom: '2px',
  },
  panelHeaderGood: {
    display: 'flex',
    alignItems: 'center',
    gap: '6px',
    color: theme.colors.success,
    marginBottom: '2px',
  },
  xIcon: {
    fontSize: '14px',
  },
  checkIcon: {
    fontSize: '14px',
  },
  panelTitle: {
    fontSize: '11px',
    fontWeight: 700,
    letterSpacing: '0.5px',
  },
  panelSubtitle: {
    fontSize: '8px',
    color: theme.colors.textLight,
    fontStyle: 'italic',
    margin: '0 0 6px 0',
  },
  flowContainer: {
    display: 'flex',
    flexDirection: 'column',
    gap: '5px',
    flex: 1,
  },
  strategyBoxEmpty: {
    backgroundColor: '#e5e7eb',
    color: theme.colors.textLight,
    padding: '5px 8px',
    fontSize: '9px',
    fontWeight: 600,
    textAlign: 'center',
    borderRadius: '4px',
    border: '2px dashed #9ca3af',
    display: 'flex',
    alignItems: 'center',
    justifyContent: 'center',
    gap: '4px',
  },
  questionIcon: {
    fontSize: '12px',
  },
  strategyBoxFull: {
    backgroundColor: theme.colors.primary,
    color: 'white',
    padding: '5px 8px',
    borderRadius: '4px',
  },
  strategyRow: {
    display: 'flex',
    alignItems: 'center',
    gap: '4px',
    justifyContent: 'center',
  },
  strategyIcon: {
    fontSize: '12px',
  },
  strategyLabel: {
    fontSize: '9px',
    fontWeight: 700,
  },
  tradeoffRow: {
    display: 'flex',
    alignItems: 'center',
    gap: '4px',
    justifyContent: 'center',
    marginTop: '2px',
  },
  tradeoffIcon: {
    fontSize: '10px',
  },
  tradeoffLabel: {
    fontSize: '7px',
    opacity: 0.9,
  },
  goalBox: {
    backgroundColor: theme.colors.accent,
    color: 'white',
    padding: '4px 8px',
    fontSize: '9px',
    fontWeight: 600,
    textAlign: 'center',
    borderRadius: '4px',
    display: 'flex',
    alignItems: 'center',
    justifyContent: 'center',
    gap: '4px',
  },
  goalBoxGood: {
    backgroundColor: theme.colors.accent,
    color: 'white',
    padding: '4px 8px',
    fontSize: '9px',
    fontWeight: 600,
    textAlign: 'center',
    borderRadius: '4px',
    display: 'flex',
    alignItems: 'center',
    justifyContent: 'center',
    gap: '4px',
  },
  goalIcon: {
    fontSize: '10px',
  },
  chaosZone: {
    backgroundColor: 'rgba(254, 202, 202, 0.5)',
    borderRadius: '4px',
    padding: '6px',
    flex: 1,
    display: 'flex',
    flexDirection: 'column',
    gap: '4px',
  },
  chaosLabel: {
    textAlign: 'center',
    fontSize: '8px',
    color: theme.colors.error,
    fontWeight: 700,
  },
  scatteredPeopleGrid: {
    display: 'grid',
    gridTemplateColumns: 'repeat(3, 1fr)',
    gap: '4px',
    padding: '4px',
  },
  personScattered: {
    display: 'flex',
    alignItems: 'center',
    justifyContent: 'center',
    gap: '2px',
    backgroundColor: 'white',
    padding: '3px 4px',
    borderRadius: '4px',
    border: `1px solid ${theme.colors.error}`,
    fontSize: '12px',
  },
  personIcon: {
    fontSize: '14px',
  },
  arrowScattered: {
    fontSize: '12px',
  },
  scatteredTactics: {
    display: 'grid',
    gridTemplateColumns: '1fr 1fr',
    gap: '3px',
  },
  tacticBad: {
    backgroundColor: 'white',
    color: theme.colors.text,
    padding: '3px 4px',
    fontSize: '7px',
    textAlign: 'center',
    borderRadius: '3px',
    border: `1px solid ${theme.colors.error}`,
  },
  funnelZone: {
    display: 'flex',
    flex: 1,
    borderRadius: '4px',
    overflow: 'hidden',
  },
  guardrailLeft: {
    width: '28px',
    backgroundColor: theme.colors.success,
    display: 'flex',
    alignItems: 'center',
    justifyContent: 'center',
  },
  guardrailRight: {
    width: '28px',
    backgroundColor: theme.colors.success,
    display: 'flex',
    alignItems: 'center',
    justifyContent: 'center',
  },
  guardrailInner: {
    display: 'flex',
    flexDirection: 'column',
    alignItems: 'center',
    gap: '2px',
  },
  guardrailIcon: {
    fontSize: '12px',
  },
  guardrailText: {
    fontSize: '5px',
    fontWeight: 700,
    color: 'white',
    textAlign: 'center',
    lineHeight: 1.1,
  },
  alignedZone: {
    flex: 1,
    backgroundColor: 'rgba(187, 247, 208, 0.5)',
    padding: '4px',
    display: 'flex',
    alignItems: 'center',
    justifyContent: 'center',
  },
  alignedPeopleGrid: {
    display: 'grid',
    gridTemplateColumns: 'repeat(3, 1fr)',
    gap: '4px',
  },
  personAligned: {
    display: 'flex',
    flexDirection: 'column',
    alignItems: 'center',
    backgroundColor: 'white',
    padding: '3px 6px',
    borderRadius: '4px',
    border: `1px solid ${theme.colors.success}`,
  },
  arrowDown: {
    fontSize: '12px',
  },
  alignedTactics: {
    display: 'grid',
    gridTemplateColumns: '1fr 1fr',
    gap: '3px',
  },
  tacticGood: {
    backgroundColor: 'white',
    color: theme.colors.text,
    padding: '3px 4px',
    fontSize: '7px',
    textAlign: 'center',
    borderRadius: '3px',
    border: `1px solid ${theme.colors.success}`,
  },
  resultBad: {
    backgroundColor: theme.colors.error,
    color: 'white',
    padding: '5px 8px',
    fontSize: '8px',
    fontWeight: 600,
    textAlign: 'center',
    borderRadius: '4px',
    display: 'flex',
    alignItems: 'center',
    justifyContent: 'center',
    gap: '4px',
  },
  resultGood: {
    backgroundColor: theme.colors.success,
    color: 'white',
    padding: '5px 8px',
    fontSize: '8px',
    fontWeight: 600,
    textAlign: 'center',
    borderRadius: '4px',
    display: 'flex',
    alignItems: 'center',
    justifyContent: 'center',
    gap: '4px',
  },
  resultIcon: {
    fontSize: '12px',
  },
  keyInsightBar: {
    backgroundColor: theme.colors.secondary,
    padding: '6px 12px',
    marginTop: '6px',
    marginLeft: '-48px',
    marginRight: '-48px',
    display: 'flex',
    alignItems: 'center',
    justifyContent: 'center',
    gap: '8px',
  },
  quoteIcon: {
    fontSize: '14px',
  },
  keyInsightText: {
    fontSize: '9px',
    color: 'white',
    margin: 0,
    textAlign: 'center',
    lineHeight: 1.3,
  }
}
