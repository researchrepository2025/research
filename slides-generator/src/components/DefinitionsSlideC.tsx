import React from 'react'
import { SlideBase } from './SlideBase'
import { theme } from '../theme'
import type { SlideContent } from '../slideContent'

// Variation C: Minimalist Executive - Maximum whitespace, essential content only
interface DefinitionsSlideCProps {
  content: SlideContent
  slideNumber: number
  totalSlides: number
}

export const DefinitionsSlideC: React.FC<DefinitionsSlideCProps> = ({ 
  content, 
  slideNumber, 
  totalSlides 
}) => {
  return (
    <SlideBase slideNumber={slideNumber} totalSlides={totalSlides} footer={content.footer}>
      {/* Clean centered header */}
      <div style={styles.header}>
        <div style={styles.accentLine} />
        <h1 style={styles.title}>{content.title}</h1>
      </div>
      
      {/* Three minimal cards */}
      <div style={styles.cardsContainer}>
        {content.sections?.map((section, idx) => (
          <div key={idx} style={styles.card}>
            <div style={styles.cardHeader}>
              <span style={styles.cardNumber}>{idx + 1}</span>
              <span style={styles.cardLabel}>{section.heading}</span>
            </div>
            <p style={styles.cardDef}>{section.definition}</p>
            <div style={styles.cardExample}>
              <span style={styles.exampleLabel}>Example:</span>
              <span style={styles.exampleText}>{section.example?.correct?.text}</span>
            </div>
          </div>
        ))}
      </div>
      
      {/* Minimal key insight */}
      {content.keyInsight && (
        <div style={styles.keyInsight}>
          <p style={styles.keyInsightText}>{content.keyInsight}</p>
        </div>
      )}
    </SlideBase>
  )
}

const styles: Record<string, React.CSSProperties> = {
  header: {
    textAlign: 'center',
    marginBottom: '32px',
  },
  accentLine: {
    width: '60px',
    height: '3px',
    backgroundColor: theme.colors.primary,
    margin: '0 auto 16px auto',
  },
  title: {
    fontSize: '32px',
    fontWeight: 700,
    color: theme.colors.secondary,
    fontFamily: theme.typography.fontFamily.heading,
    margin: 0,
    letterSpacing: '-0.5px',
  },
  cardsContainer: {
    display: 'flex',
    gap: '32px',
    flex: 1,
    padding: '0 16px',
  },
  card: {
    flex: 1,
    display: 'flex',
    flexDirection: 'column',
    padding: '24px',
    backgroundColor: 'white',
    borderRadius: '8px',
    boxShadow: '0 2px 8px rgba(0,0,0,0.06)',
    border: `1px solid ${theme.colors.lightGray}`,
  },
  cardHeader: {
    display: 'flex',
    alignItems: 'center',
    gap: '12px',
    marginBottom: '16px',
  },
  cardNumber: {
    width: '28px',
    height: '28px',
    borderRadius: '50%',
    backgroundColor: theme.colors.primary,
    color: 'white',
    display: 'flex',
    alignItems: 'center',
    justifyContent: 'center',
    fontSize: '14px',
    fontWeight: 700,
  },
  cardLabel: {
    fontSize: '16px',
    fontWeight: 700,
    color: theme.colors.secondary,
    letterSpacing: '1px',
  },
  cardDef: {
    fontSize: '13px',
    color: theme.colors.text,
    lineHeight: 1.6,
    margin: 0,
    marginBottom: '16px',
    flex: 1,
  },
  cardExample: {
    backgroundColor: theme.colors.lightGray,
    padding: '12px',
    borderRadius: '4px',
    borderLeft: `3px solid ${theme.colors.success}`,
  },
  exampleLabel: {
    display: 'block',
    fontSize: '10px',
    fontWeight: 700,
    color: theme.colors.success,
    marginBottom: '4px',
    textTransform: 'uppercase',
    letterSpacing: '0.5px',
  },
  exampleText: {
    fontSize: '11px',
    color: theme.colors.text,
    lineHeight: 1.4,
    fontStyle: 'italic',
  },
  keyInsight: {
    textAlign: 'center',
    marginTop: '24px',
    padding: '16px 32px',
    backgroundColor: theme.colors.lightGray,
    borderRadius: '4px',
  },
  keyInsightText: {
    fontSize: '13px',
    color: theme.colors.text,
    fontWeight: 500,
    margin: 0,
  }
}
