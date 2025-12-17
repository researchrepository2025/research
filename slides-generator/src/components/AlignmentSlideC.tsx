import React from 'react'
import { SlideBase } from './SlideBase'
import { theme } from '../theme'
import type { SlideContent } from '../slideContent'

// Variation C: Pyramid/Hierarchy Diagram - Strategy cascading down
interface AlignmentSlideCProps {
  content: SlideContent
  slideNumber: number
  totalSlides: number
}

export const AlignmentSlideC: React.FC<AlignmentSlideCProps> = ({ 
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
      
      {/* Two pyramid diagrams side by side */}
      <div style={styles.pyramidsContainer}>
        {/* WITHOUT STRATEGY pyramid */}
        <div style={styles.pyramidSection}>
          <div style={styles.pyramidLabel}>
            <span style={styles.xIcon}>✗</span> WITHOUT STRATEGY
          </div>
          <div style={styles.pyramid}>
            <div style={styles.pyramidTopEmpty}>
              <span style={styles.pyramidText}>?</span>
              <span style={styles.pyramidSubtext}>No Strategy</span>
            </div>
            <div style={styles.pyramidMidBad}>
              <span style={styles.pyramidText}>🎯 "Grow Revenue"</span>
            </div>
            <div style={styles.pyramidBottomScatter}>
              <div style={styles.scatterTacticBad}>Cut costs</div>
              <div style={styles.scatterTacticBad}>Enterprise</div>
              <div style={styles.scatterTacticBad}>Global</div>
              <div style={styles.scatterTacticBad}>Discount</div>
            </div>
            <div style={styles.pyramidResult}>
              <span style={styles.resultBadText}>Conflicting priorities</span>
            </div>
          </div>
        </div>
        
        {/* WITH STRATEGY pyramid */}
        <div style={styles.pyramidSection}>
          <div style={styles.pyramidLabelGood}>
            <span style={styles.checkIcon}>✓</span> WITH STRATEGY
          </div>
          <div style={styles.pyramid}>
            <div style={styles.pyramidTopFull}>
              <span style={styles.pyramidText}>Win Mid-Market Mfg</span>
              <span style={styles.pyramidSubtext}>NOT enterprise, NOT horizontal</span>
            </div>
            <div style={styles.pyramidMidGood}>
              <span style={styles.pyramidText}>🎯 500 Mfg Customers</span>
            </div>
            <div style={styles.pyramidBottomAlign}>
              <div style={styles.alignTacticGood}>NAM sponsor</div>
              <div style={styles.alignTacticGood}>Vertical reps</div>
              <div style={styles.alignTacticGood}>Mfg LinkedIn</div>
              <div style={styles.alignTacticGood}>Case studies</div>
            </div>
            <div style={styles.pyramidResultGood}>
              <span style={styles.resultGoodText}>Compounding advantage</span>
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
    marginBottom: '12px',
  },
  title: {
    fontSize: '22px',
    fontWeight: 700,
    color: theme.colors.secondary,
    fontFamily: theme.typography.fontFamily.heading,
    margin: 0,
  },
  pyramidsContainer: {
    display: 'flex',
    gap: '24px',
    flex: 1,
  },
  pyramidSection: {
    flex: 1,
    display: 'flex',
    flexDirection: 'column',
  },
  pyramidLabel: {
    display: 'flex',
    alignItems: 'center',
    justifyContent: 'center',
    gap: '8px',
    color: theme.colors.error,
    fontSize: '12px',
    fontWeight: 700,
    marginBottom: '12px',
    padding: '6px 12px',
    backgroundColor: '#fee2e2',
    borderRadius: '4px',
  },
  pyramidLabelGood: {
    display: 'flex',
    alignItems: 'center',
    justifyContent: 'center',
    gap: '8px',
    color: theme.colors.success,
    fontSize: '12px',
    fontWeight: 700,
    marginBottom: '12px',
    padding: '6px 12px',
    backgroundColor: '#dcfce7',
    borderRadius: '4px',
  },
  xIcon: {
    fontSize: '14px',
  },
  checkIcon: {
    fontSize: '14px',
  },
  pyramid: {
    display: 'flex',
    flexDirection: 'column',
    alignItems: 'center',
    gap: '8px',
    flex: 1,
  },
  pyramidTopEmpty: {
    width: '60%',
    backgroundColor: '#e5e7eb',
    padding: '12px',
    borderRadius: '4px',
    textAlign: 'center',
    border: '2px dashed #9ca3af',
  },
  pyramidTopFull: {
    width: '60%',
    backgroundColor: theme.colors.primary,
    padding: '12px',
    borderRadius: '4px',
    textAlign: 'center',
    color: 'white',
  },
  pyramidText: {
    fontSize: '12px',
    fontWeight: 700,
    display: 'block',
  },
  pyramidSubtext: {
    fontSize: '9px',
    opacity: 0.8,
    marginTop: '2px',
    display: 'block',
  },
  pyramidMidBad: {
    width: '80%',
    backgroundColor: theme.colors.accent,
    padding: '10px',
    borderRadius: '4px',
    textAlign: 'center',
    color: 'white',
  },
  pyramidMidGood: {
    width: '80%',
    backgroundColor: theme.colors.accent,
    padding: '10px',
    borderRadius: '4px',
    textAlign: 'center',
    color: 'white',
  },
  pyramidBottomScatter: {
    width: '100%',
    display: 'flex',
    flexWrap: 'wrap',
    gap: '6px',
    justifyContent: 'center',
    padding: '8px',
    backgroundColor: '#fef2f2',
    borderRadius: '4px',
  },
  pyramidBottomAlign: {
    width: '100%',
    display: 'flex',
    flexWrap: 'wrap',
    gap: '6px',
    justifyContent: 'center',
    padding: '8px',
    backgroundColor: '#f0fdf4',
    borderRadius: '4px',
  },
  scatterTacticBad: {
    padding: '6px 10px',
    backgroundColor: 'white',
    border: `1px solid ${theme.colors.error}`,
    borderRadius: '3px',
    fontSize: '10px',
    color: theme.colors.text,
    transform: 'rotate(-3deg)',
  },
  alignTacticGood: {
    padding: '6px 10px',
    backgroundColor: 'white',
    border: `1px solid ${theme.colors.success}`,
    borderRadius: '3px',
    fontSize: '10px',
    color: theme.colors.text,
  },
  pyramidResult: {
    width: '70%',
    backgroundColor: theme.colors.error,
    padding: '8px 12px',
    borderRadius: '4px',
    textAlign: 'center',
    marginTop: '4px',
  },
  pyramidResultGood: {
    width: '70%',
    backgroundColor: theme.colors.success,
    padding: '8px 12px',
    borderRadius: '4px',
    textAlign: 'center',
    marginTop: '4px',
  },
  resultBadText: {
    color: 'white',
    fontSize: '11px',
    fontWeight: 600,
  },
  resultGoodText: {
    color: 'white',
    fontSize: '11px',
    fontWeight: 600,
  },
  quoteBar: {
    backgroundColor: theme.colors.secondary,
    padding: '10px 16px',
    marginTop: '12px',
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
