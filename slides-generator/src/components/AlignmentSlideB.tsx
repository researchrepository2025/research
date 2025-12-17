import React from 'react'
import { SlideBase } from './SlideBase'
import { theme } from '../theme'
import type { SlideContent } from '../slideContent'

// Variation B: Before/After Visual Flow - Horizontal timeline style
interface AlignmentSlideBProps {
  content: SlideContent
  slideNumber: number
  totalSlides: number
}

export const AlignmentSlideB: React.FC<AlignmentSlideBProps> = ({ 
  content, 
  slideNumber, 
  totalSlides 
}) => {
  return (
    <SlideBase slideNumber={slideNumber} totalSlides={totalSlides} footer={content.footer}>
      {/* Title */}
      <div style={styles.header}>
        <h1 style={styles.title}>{content.title}</h1>
      </div>
      
      {/* Two horizontal flow diagrams stacked */}
      <div style={styles.flowsContainer}>
        {/* WITHOUT STRATEGY flow */}
        <div style={styles.flowSection}>
          <div style={styles.flowLabel}>
            <span style={styles.xIcon}>✗</span> WITHOUT STRATEGY
          </div>
          <div style={styles.flowDiagram}>
            <div style={styles.nodeEmpty}>
              <span style={styles.nodeLabel}>No Strategy</span>
            </div>
            <div style={styles.arrowBad}>→</div>
            <div style={styles.nodeGoal}>
              <span style={styles.nodeLabel}>🎯 Grow Revenue</span>
            </div>
            <div style={styles.arrowBad}>→</div>
            <div style={styles.tacticsScatter}>
              <div style={styles.tacticBadSmall}>Cut costs</div>
              <div style={styles.tacticBadSmall}>Enterprise</div>
              <div style={styles.tacticBadSmall}>Global</div>
              <div style={styles.tacticBadSmall}>Discount</div>
            </div>
            <div style={styles.arrowBad}>→</div>
            <div style={styles.resultBad}>
              <span style={styles.resultText}>Chaos</span>
            </div>
          </div>
        </div>
        
        {/* WITH STRATEGY flow */}
        <div style={styles.flowSection}>
          <div style={styles.flowLabelGood}>
            <span style={styles.checkIcon}>✓</span> WITH STRATEGY
          </div>
          <div style={styles.flowDiagram}>
            <div style={styles.nodeStrategy}>
              <span style={styles.nodeLabel}>Win Mid-Market</span>
              <span style={styles.nodeSubLabel}>NOT enterprise</span>
            </div>
            <div style={styles.arrowGood}>→</div>
            <div style={styles.nodeGoalGood}>
              <span style={styles.nodeLabel}>🎯 500 Customers</span>
            </div>
            <div style={styles.arrowGood}>→</div>
            <div style={styles.tacticsAlign}>
              <div style={styles.tacticGoodSmall}>NAM</div>
              <div style={styles.tacticGoodSmall}>Vertical</div>
              <div style={styles.tacticGoodSmall}>LinkedIn</div>
              <div style={styles.tacticGoodSmall}>Cases</div>
            </div>
            <div style={styles.arrowGood}>→</div>
            <div style={styles.resultGood}>
              <span style={styles.resultText}>Aligned</span>
            </div>
          </div>
        </div>
      </div>
      
      {/* Quote */}
      {content.keyInsight && (
        <div style={styles.quoteBar}>
          <p style={styles.quoteText}>{content.keyInsight}</p>
        </div>
      )}
    </SlideBase>
  )
}

const styles: Record<string, React.CSSProperties> = {
  header: {
    textAlign: 'center',
    marginBottom: '16px',
    borderBottom: `3px solid ${theme.colors.primary}`,
    paddingBottom: '12px',
  },
  title: {
    fontSize: '22px',
    fontWeight: 700,
    color: theme.colors.secondary,
    fontFamily: theme.typography.fontFamily.heading,
    margin: 0,
  },
  flowsContainer: {
    flex: 1,
    display: 'flex',
    flexDirection: 'column',
    gap: '16px',
  },
  flowSection: {
    flex: 1,
    backgroundColor: theme.colors.lightGray,
    borderRadius: '8px',
    padding: '16px 20px',
  },
  flowLabel: {
    display: 'flex',
    alignItems: 'center',
    gap: '8px',
    color: theme.colors.error,
    fontSize: '13px',
    fontWeight: 700,
    marginBottom: '12px',
  },
  flowLabelGood: {
    display: 'flex',
    alignItems: 'center',
    gap: '8px',
    color: theme.colors.success,
    fontSize: '13px',
    fontWeight: 700,
    marginBottom: '12px',
  },
  xIcon: {
    fontSize: '14px',
  },
  checkIcon: {
    fontSize: '14px',
  },
  flowDiagram: {
    display: 'flex',
    alignItems: 'center',
    gap: '8px',
  },
  nodeEmpty: {
    backgroundColor: '#e5e7eb',
    padding: '10px 14px',
    borderRadius: '6px',
    border: '2px dashed #9ca3af',
    textAlign: 'center',
  },
  nodeStrategy: {
    backgroundColor: theme.colors.primary,
    padding: '10px 14px',
    borderRadius: '6px',
    textAlign: 'center',
    color: 'white',
  },
  nodeGoal: {
    backgroundColor: theme.colors.accent,
    padding: '10px 14px',
    borderRadius: '6px',
    textAlign: 'center',
    color: 'white',
  },
  nodeGoalGood: {
    backgroundColor: theme.colors.accent,
    padding: '10px 14px',
    borderRadius: '6px',
    textAlign: 'center',
    color: 'white',
  },
  nodeLabel: {
    fontSize: '11px',
    fontWeight: 600,
    display: 'block',
  },
  nodeSubLabel: {
    fontSize: '9px',
    opacity: 0.8,
    marginTop: '2px',
    display: 'block',
  },
  arrowBad: {
    color: theme.colors.error,
    fontSize: '20px',
    fontWeight: 700,
  },
  arrowGood: {
    color: theme.colors.success,
    fontSize: '20px',
    fontWeight: 700,
  },
  tacticsScatter: {
    display: 'grid',
    gridTemplateColumns: '1fr 1fr',
    gap: '4px',
    transform: 'rotate(-5deg)',
  },
  tacticsAlign: {
    display: 'grid',
    gridTemplateColumns: '1fr 1fr',
    gap: '4px',
  },
  tacticBadSmall: {
    backgroundColor: 'white',
    border: `1px solid ${theme.colors.error}`,
    padding: '4px 8px',
    borderRadius: '3px',
    fontSize: '9px',
    textAlign: 'center',
    color: theme.colors.text,
  },
  tacticGoodSmall: {
    backgroundColor: 'white',
    border: `1px solid ${theme.colors.success}`,
    padding: '4px 8px',
    borderRadius: '3px',
    fontSize: '9px',
    textAlign: 'center',
    color: theme.colors.text,
  },
  resultBad: {
    backgroundColor: theme.colors.error,
    padding: '12px 16px',
    borderRadius: '6px',
    textAlign: 'center',
    color: 'white',
  },
  resultGood: {
    backgroundColor: theme.colors.success,
    padding: '12px 16px',
    borderRadius: '6px',
    textAlign: 'center',
    color: 'white',
  },
  resultText: {
    fontSize: '12px',
    fontWeight: 700,
  },
  quoteBar: {
    backgroundColor: theme.colors.secondary,
    padding: '12px 20px',
    marginTop: '16px',
    marginLeft: '-48px',
    marginRight: '-48px',
  },
  quoteText: {
    fontSize: '11px',
    color: 'white',
    margin: 0,
    textAlign: 'center',
    lineHeight: 1.4,
  }
}
