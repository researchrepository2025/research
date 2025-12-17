import React from 'react'
import { SlideBase } from './SlideBase'
import { theme } from '../theme'
import type { SlideContent } from '../slideContent'

interface ComparisonSlideProps {
  content: SlideContent
  slideNumber: number
  totalSlides: number
}

export const ComparisonSlide: React.FC<ComparisonSlideProps> = ({ 
  content, 
  slideNumber, 
  totalSlides 
}) => {
  const section = content.sections?.[0]
  const isWithStrategy = content.id === 'with-strategy'
  
  return (
    <SlideBase slideNumber={slideNumber} totalSlides={totalSlides} footer={content.footer}>
      <div style={styles.titleBar}>
        <h1 style={styles.title}>{content.title}</h1>
      </div>
      
      {section && (
        <div style={styles.comparisonContainer}>
          <div style={{
            ...styles.panel,
            borderLeft: `4px solid ${isWithStrategy ? theme.colors.success : theme.colors.error}`,
          }}>
            <div style={{
              ...styles.panelHeader,
              color: isWithStrategy ? theme.colors.success : theme.colors.error,
            }}>
              <span style={styles.statusIcon}>{isWithStrategy ? '✓' : '✗'}</span>
              {section.heading}
            </div>
            <p style={styles.subheading}>{section.subheading}</p>
            
            <div style={styles.flowContainer}>
              {section.items?.map((item, idx) => {
                const isGoal = item.includes('Goal:') || item.includes('Strategy:')
                const isResult = item.includes('Result:')
                const isArrow = item.startsWith('→')
                
                return (
                  <div key={idx} style={{
                    ...styles.flowItem,
                    ...(isGoal && styles.goalItem),
                    ...(isResult && (isWithStrategy ? styles.resultSuccess : styles.resultError)),
                    ...(isArrow && styles.arrowItem),
                  }}>
                    {item}
                  </div>
                )
              })}
            </div>
          </div>
        </div>
      )}
    </SlideBase>
  )
}

const styles: Record<string, React.CSSProperties> = {
  titleBar: {
    borderBottom: `3px solid ${theme.colors.primary}`,
    paddingBottom: '12px',
    marginBottom: '20px',
  },
  title: {
    fontSize: '22px',
    fontWeight: 700,
    color: theme.colors.secondary,
    fontFamily: theme.typography.fontFamily.heading,
    margin: 0,
    lineHeight: 1.3,
  },
  comparisonContainer: {
    flex: 1,
    display: 'flex',
    gap: '24px',
  },
  panel: {
    flex: 1,
    backgroundColor: theme.colors.lightGray,
    padding: '24px',
    borderRadius: '4px',
  },
  panelHeader: {
    display: 'flex',
    alignItems: 'center',
    gap: '8px',
    fontSize: '16px',
    fontWeight: 700,
    marginBottom: '8px',
    letterSpacing: '0.5px',
  },
  statusIcon: {
    fontSize: '18px',
  },
  subheading: {
    fontSize: '13px',
    color: theme.colors.textLight,
    margin: 0,
    marginBottom: '20px',
    fontStyle: 'italic',
  },
  flowContainer: {
    display: 'flex',
    flexDirection: 'column',
    gap: '10px',
  },
  flowItem: {
    fontSize: '14px',
    color: theme.colors.text,
    fontFamily: theme.typography.fontFamily.body,
    lineHeight: 1.4,
    padding: '8px 12px',
    backgroundColor: 'white',
    borderRadius: '4px',
  },
  goalItem: {
    backgroundColor: theme.colors.primary,
    color: 'white',
    fontWeight: 600,
  },
  arrowItem: {
    backgroundColor: 'transparent',
    paddingLeft: '24px',
    color: theme.colors.textLight,
  },
  resultSuccess: {
    backgroundColor: theme.colors.success,
    color: 'white',
    fontWeight: 600,
  },
  resultError: {
    backgroundColor: theme.colors.error,
    color: 'white',
    fontWeight: 600,
  }
}
