import React from 'react'
import { SlideBase } from './SlideBase'
import { theme } from '../theme'
import type { SlideContent } from '../slideContent'

interface FrameworkSlideProps {
  content: SlideContent
  slideNumber: number
  totalSlides: number
}

export const FrameworkSlide: React.FC<FrameworkSlideProps> = ({ 
  content, 
  slideNumber, 
  totalSlides 
}) => {
  const section = content.sections?.[0]
  
  return (
    <SlideBase slideNumber={slideNumber} totalSlides={totalSlides} footer={content.footer}>
      <div style={styles.titleBar}>
        <h1 style={styles.title}>{content.title}</h1>
      </div>
      
      {section && (
        <div style={styles.frameworkContainer}>
          <div style={styles.headerSection}>
            <div style={styles.labelBadge}>{section.heading}</div>
            <p style={styles.definition}>{section.subheading}</p>
          </div>
          
          {section.example && (
            <div style={styles.examplesRow}>
              {section.example.correct && (
                <div style={styles.exampleBox}>
                  <div style={styles.correctLabel}>
                    <span style={styles.checkmark}>✓</span>
                    {section.example.correct.label}
                  </div>
                  <p style={styles.exampleText}>{section.example.correct.text}</p>
                </div>
              )}
              
              {section.example.incorrect && (
                <div style={styles.exampleBox}>
                  <div style={styles.incorrectLabel}>
                    <span style={styles.xmark}>✗</span>
                    {section.example.incorrect.label}
                  </div>
                  <p style={styles.exampleText}>{section.example.incorrect.text}</p>
                  {section.example.incorrect.note && (
                    <p style={styles.noteText}>↳ {section.example.incorrect.note}</p>
                  )}
                </div>
              )}
            </div>
          )}
        </div>
      )}
    </SlideBase>
  )
}

const styles: Record<string, React.CSSProperties> = {
  titleBar: {
    borderBottom: `3px solid ${theme.colors.primary}`,
    paddingBottom: '12px',
    marginBottom: '24px',
  },
  title: {
    fontSize: '22px',
    fontWeight: 700,
    color: theme.colors.secondary,
    fontFamily: theme.typography.fontFamily.heading,
    margin: 0,
    lineHeight: 1.3,
  },
  frameworkContainer: {
    flex: 1,
    display: 'flex',
    flexDirection: 'column',
  },
  headerSection: {
    marginBottom: '24px',
  },
  labelBadge: {
    display: 'inline-block',
    backgroundColor: theme.colors.primary,
    color: 'white',
    padding: '6px 16px',
    fontSize: '14px',
    fontWeight: 700,
    letterSpacing: '1px',
    marginBottom: '12px',
  },
  definition: {
    fontSize: '16px',
    color: theme.colors.text,
    fontFamily: theme.typography.fontFamily.body,
    margin: 0,
    lineHeight: 1.5,
  },
  examplesRow: {
    display: 'flex',
    gap: '24px',
    flex: 1,
  },
  exampleBox: {
    flex: 1,
    backgroundColor: theme.colors.lightGray,
    padding: '20px',
    borderRadius: '4px',
  },
  correctLabel: {
    display: 'flex',
    alignItems: 'center',
    gap: '8px',
    color: theme.colors.success,
    fontSize: '13px',
    fontWeight: 700,
    marginBottom: '12px',
    letterSpacing: '0.5px',
  },
  incorrectLabel: {
    display: 'flex',
    alignItems: 'center',
    gap: '8px',
    color: theme.colors.error,
    fontSize: '13px',
    fontWeight: 700,
    marginBottom: '12px',
    letterSpacing: '0.5px',
  },
  checkmark: {
    fontSize: '16px',
  },
  xmark: {
    fontSize: '16px',
  },
  exampleText: {
    fontSize: '14px',
    color: theme.colors.text,
    fontFamily: theme.typography.fontFamily.body,
    margin: 0,
    lineHeight: 1.5,
    fontStyle: 'italic',
  },
  noteText: {
    fontSize: '12px',
    color: theme.colors.textLight,
    fontFamily: theme.typography.fontFamily.body,
    margin: 0,
    marginTop: '12px',
    lineHeight: 1.4,
  }
}
