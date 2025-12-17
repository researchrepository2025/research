import React from 'react'
import { SlideBase } from './SlideBase'
import { theme } from '../theme'
import type { SlideContent } from '../slideContent'

// Variation B: McKinsey Matrix Style - Table layout with more whitespace
interface DefinitionsSlideBProps {
  content: SlideContent
  slideNumber: number
  totalSlides: number
}

export const DefinitionsSlideB: React.FC<DefinitionsSlideBProps> = ({ 
  content, 
  slideNumber, 
  totalSlides 
}) => {
  return (
    <SlideBase slideNumber={slideNumber} totalSlides={totalSlides} footer={content.footer}>
      {/* Header */}
      <div style={styles.header}>
        <h1 style={styles.title}>{content.title}</h1>
        {content.subtitle && <p style={styles.subtitle}>{content.subtitle}</p>}
      </div>
      
      {/* Matrix-style table */}
      <div style={styles.matrixContainer}>
        {/* Header row */}
        <div style={styles.headerRow}>
          <div style={styles.headerCellFirst}></div>
          {content.sections?.map((section, idx) => (
            <div key={idx} style={styles.headerCell}>
              <span style={styles.headerLabel}>{section.heading}</span>
              <span style={styles.headerSub}>{section.subheading}</span>
            </div>
          ))}
        </div>
        
        {/* Definition row */}
        <div style={styles.bodyRow}>
          <div style={styles.rowLabel}>Definition</div>
          {content.sections?.map((section, idx) => (
            <div key={idx} style={styles.bodyCell}>
              <p style={styles.defText}>{section.definition}</p>
            </div>
          ))}
        </div>
        
        {/* Correct example row */}
        <div style={styles.bodyRow}>
          <div style={{...styles.rowLabel, ...styles.correctRowLabel}}>
            <span style={styles.checkIcon}>✓</span> Correct
          </div>
          {content.sections?.map((section, idx) => (
            <div key={idx} style={{...styles.bodyCell, ...styles.correctCell}}>
              <p style={styles.exampleText}>{section.example?.correct?.text}</p>
            </div>
          ))}
        </div>
        
        {/* Incorrect example row */}
        <div style={styles.bodyRow}>
          <div style={{...styles.rowLabel, ...styles.incorrectRowLabel}}>
            <span style={styles.xIcon}>✗</span> Incorrect
          </div>
          {content.sections?.map((section, idx) => (
            <div key={idx} style={{...styles.bodyCell, ...styles.incorrectCell}}>
              <p style={styles.exampleText}>{section.example?.incorrect?.text}</p>
              {section.example?.incorrect?.note && (
                <p style={styles.noteText}>↳ {section.example.incorrect.note}</p>
              )}
            </div>
          ))}
        </div>
      </div>
      
      {/* Key insight */}
      {content.keyInsight && (
        <div style={styles.keyInsightBar}>
          <p style={styles.keyInsightText}>{content.keyInsight}</p>
        </div>
      )}
    </SlideBase>
  )
}

const styles: Record<string, React.CSSProperties> = {
  header: {
    textAlign: 'center',
    marginBottom: '20px',
    borderBottom: `3px solid ${theme.colors.primary}`,
    paddingBottom: '12px',
  },
  title: {
    fontSize: '26px',
    fontWeight: 700,
    color: theme.colors.secondary,
    fontFamily: theme.typography.fontFamily.heading,
    margin: 0,
  },
  subtitle: {
    fontSize: '14px',
    color: theme.colors.textLight,
    fontFamily: theme.typography.fontFamily.body,
    margin: '6px 0 0 0',
  },
  matrixContainer: {
    flex: 1,
    display: 'flex',
    flexDirection: 'column',
  },
  headerRow: {
    display: 'flex',
    backgroundColor: theme.colors.primary,
  },
  headerCellFirst: {
    width: '100px',
    flexShrink: 0,
    backgroundColor: theme.colors.secondary,
  },
  headerCell: {
    flex: 1,
    padding: '12px 16px',
    display: 'flex',
    flexDirection: 'column',
    alignItems: 'center',
    borderRight: '1px solid rgba(255,255,255,0.2)',
  },
  headerLabel: {
    color: 'white',
    fontSize: '14px',
    fontWeight: 700,
    letterSpacing: '1px',
  },
  headerSub: {
    color: 'rgba(255,255,255,0.8)',
    fontSize: '10px',
    marginTop: '2px',
    fontStyle: 'italic',
  },
  bodyRow: {
    display: 'flex',
    borderBottom: `1px solid ${theme.colors.lightGray}`,
  },
  rowLabel: {
    width: '100px',
    flexShrink: 0,
    padding: '12px',
    backgroundColor: theme.colors.lightGray,
    fontSize: '11px',
    fontWeight: 600,
    color: theme.colors.text,
    display: 'flex',
    alignItems: 'center',
    justifyContent: 'center',
  },
  correctRowLabel: {
    backgroundColor: '#dcfce7',
    color: theme.colors.success,
  },
  incorrectRowLabel: {
    backgroundColor: '#fee2e2',
    color: theme.colors.error,
  },
  checkIcon: {
    marginRight: '4px',
    fontSize: '12px',
  },
  xIcon: {
    marginRight: '4px',
    fontSize: '12px',
  },
  bodyCell: {
    flex: 1,
    padding: '12px 16px',
    borderRight: `1px solid ${theme.colors.lightGray}`,
  },
  correctCell: {
    backgroundColor: '#f0fdf4',
  },
  incorrectCell: {
    backgroundColor: '#fef2f2',
  },
  defText: {
    fontSize: '11px',
    color: theme.colors.text,
    lineHeight: 1.5,
    margin: 0,
  },
  exampleText: {
    fontSize: '10px',
    color: theme.colors.text,
    lineHeight: 1.4,
    margin: 0,
    fontStyle: 'italic',
  },
  noteText: {
    fontSize: '9px',
    color: theme.colors.textLight,
    margin: '6px 0 0 0',
    lineHeight: 1.3,
  },
  keyInsightBar: {
    backgroundColor: theme.colors.secondary,
    padding: '10px 16px',
    marginTop: 'auto',
    marginLeft: '-48px',
    marginRight: '-48px',
  },
  keyInsightText: {
    fontSize: '11px',
    color: 'white',
    fontWeight: 500,
    margin: 0,
    textAlign: 'center',
  }
}
