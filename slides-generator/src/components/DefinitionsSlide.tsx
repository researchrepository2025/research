import React from 'react'
import { SlideBase } from './SlideBase'
import { theme } from '../theme'
import type { SlideContent } from '../slideContent'

interface DefinitionsSlideProps {
  content: SlideContent
  slideNumber: number
  totalSlides: number
}

export const DefinitionsSlide: React.FC<DefinitionsSlideProps> = ({ 
  content, 
  slideNumber, 
  totalSlides 
}) => {
  const footerText = content.sources?.map(s => s.text).join(' | ') || content.footer
  
  // Icons for each section
  const sectionIcons = ['🎯', '📊', '⚡']
  const componentIcons = {
    STRATEGY: ['🗺️', '🏆', '🚫', '🔗'],
    GOALS: ['📌', '📏', '✅', '🎯', '⏰'],
    TACTICS: ['📅', '🔧', '🔄', '👤', '📈']
  }
  
  return (
    <SlideBase slideNumber={slideNumber} totalSlides={totalSlides} footer={footerText}>
      {/* Header */}
      <div style={styles.header}>
        <h1 style={styles.title}>{content.title}</h1>
        {content.subtitle && <p style={styles.subtitle}>{content.subtitle}</p>}
      </div>
      
      {/* Visual hierarchy diagram */}
      <div style={styles.hierarchyBar}>
        <div style={styles.hierarchyItem}>
          <span style={styles.hierarchyIcon}>🎯</span>
          <span style={styles.hierarchyLabel}>STRATEGY</span>
          <span style={styles.hierarchyArrow}>→</span>
        </div>
        <div style={styles.hierarchyItem}>
          <span style={styles.hierarchyIcon}>📊</span>
          <span style={styles.hierarchyLabel}>GOALS</span>
          <span style={styles.hierarchyArrow}>→</span>
        </div>
        <div style={styles.hierarchyItem}>
          <span style={styles.hierarchyIcon}>⚡</span>
          <span style={styles.hierarchyLabel}>TACTICS</span>
        </div>
      </div>
      
      {/* Three-column definitions */}
      <div style={styles.columnsContainer}>
        {content.sections?.map((section, idx) => {
          const icons = componentIcons[section.heading as keyof typeof componentIcons] || []
          return (
            <div key={idx} style={styles.column}>
              {/* Section header with icon */}
              <div style={styles.sectionHeader}>
                <div style={styles.labelRow}>
                  <span style={styles.sectionIcon}>{sectionIcons[idx]}</span>
                  <div style={styles.labelBadge}>{section.heading}</div>
                </div>
                <p style={styles.subheading}>{section.subheading}</p>
              </div>
              
              {/* Definition with icon */}
              <div style={styles.definitionBox}>
                <div style={styles.defHeader}>
                  <span style={styles.defIcon}>📋</span>
                  <span style={styles.defLabel}>DEFINITION</span>
                </div>
                <p style={styles.defText}>{section.definition}</p>
              </div>
              
              {/* Components with icons */}
              {section.components && (
                <div style={styles.componentsBox}>
                  <div style={styles.componentsLabel}>
                    <span style={styles.compIcon}>🔑</span> KEY COMPONENTS
                  </div>
                  <div style={styles.componentsList}>
                    {section.components.slice(0, 3).map((comp, i) => {
                      const parts = comp.split(':')
                      return (
                        <div key={i} style={styles.componentItem}>
                          <span style={styles.componentIcon}>{icons[i] || '•'}</span>
                          <span style={styles.componentText}>
                            <strong>{parts[0]}</strong>
                          </span>
                        </div>
                      )
                    })}
                  </div>
                </div>
              )}
              
              {/* Examples with icons */}
              {section.examples && (
                <div style={styles.examplesContainer}>
                  {/* Correct example */}
                  <div style={styles.correctBox}>
                    <div style={styles.correctLabel}>
                      <span style={styles.checkIcon}>✅</span> CORRECT
                    </div>
                    <p style={styles.exampleText}>
                      {section.examples.correct[0]?.text.substring(0, 80)}...
                    </p>
                  </div>
                  
                  {/* Incorrect example */}
                  <div style={styles.incorrectBox}>
                    <div style={styles.incorrectLabel}>
                      <span style={styles.xIcon}>❌</span> INCORRECT
                    </div>
                    <p style={styles.exampleText}>
                      {section.examples.incorrect[0]?.text}
                    </p>
                    {section.examples.incorrect[0]?.note && (
                      <p style={styles.noteText}>
                        <span style={styles.noteIcon}>⚠️</span> {section.examples.incorrect[0].note}
                      </p>
                    )}
                  </div>
                </div>
              )}
            </div>
          )
        })}
      </div>
      
      {/* Key insight footer */}
      {content.keyInsight && (
        <div style={styles.keyInsightBar}>
          <span style={styles.insightIcon}>💡</span>
          <p style={styles.keyInsightText}>{content.keyInsight}</p>
        </div>
      )}
    </SlideBase>
  )
}

const styles: Record<string, React.CSSProperties> = {
  header: {
    textAlign: 'center',
    marginBottom: '8px',
  },
  title: {
    fontSize: '20px',
    fontWeight: 700,
    color: theme.colors.secondary,
    fontFamily: theme.typography.fontFamily.heading,
    margin: 0,
  },
  subtitle: {
    fontSize: '11px',
    color: theme.colors.textLight,
    fontFamily: theme.typography.fontFamily.body,
    margin: '2px 0 0 0',
  },
  hierarchyBar: {
    display: 'flex',
    justifyContent: 'center',
    alignItems: 'center',
    gap: '8px',
    backgroundColor: theme.colors.lightGray,
    padding: '6px 16px',
    borderRadius: '20px',
    marginBottom: '10px',
    width: 'fit-content',
    margin: '0 auto 10px auto',
  },
  hierarchyItem: {
    display: 'flex',
    alignItems: 'center',
    gap: '4px',
  },
  hierarchyIcon: {
    fontSize: '14px',
  },
  hierarchyLabel: {
    fontSize: '10px',
    fontWeight: 700,
    color: theme.colors.primary,
  },
  hierarchyArrow: {
    fontSize: '12px',
    color: theme.colors.mediumGray,
    marginLeft: '8px',
  },
  columnsContainer: {
    display: 'flex',
    gap: '10px',
    flex: 1,
    overflow: 'hidden',
  },
  column: {
    flex: 1,
    display: 'flex',
    flexDirection: 'column',
    borderLeft: `3px solid ${theme.colors.primary}`,
    paddingLeft: '8px',
    overflow: 'hidden',
  },
  sectionHeader: {
    marginBottom: '4px',
  },
  labelRow: {
    display: 'flex',
    alignItems: 'center',
    gap: '6px',
  },
  sectionIcon: {
    fontSize: '16px',
  },
  labelBadge: {
    display: 'inline-block',
    backgroundColor: theme.colors.primary,
    color: 'white',
    padding: '2px 8px',
    fontSize: '10px',
    fontWeight: 700,
    letterSpacing: '0.5px',
  },
  subheading: {
    fontSize: '9px',
    color: theme.colors.textLight,
    fontStyle: 'italic',
    margin: '2px 0 0 0',
  },
  definitionBox: {
    backgroundColor: theme.colors.lightGray,
    padding: '5px 6px',
    marginBottom: '4px',
    borderRadius: '3px',
  },
  defHeader: {
    display: 'flex',
    alignItems: 'center',
    gap: '4px',
    marginBottom: '2px',
  },
  defIcon: {
    fontSize: '10px',
  },
  defLabel: {
    fontSize: '8px',
    fontWeight: 700,
    color: theme.colors.primary,
    letterSpacing: '0.5px',
  },
  defText: {
    fontSize: '8px',
    color: theme.colors.text,
    lineHeight: 1.3,
    margin: 0,
  },
  componentsBox: {
    marginBottom: '4px',
  },
  componentsLabel: {
    fontSize: '8px',
    fontWeight: 700,
    color: theme.colors.primary,
    letterSpacing: '0.5px',
    marginBottom: '2px',
    display: 'flex',
    alignItems: 'center',
    gap: '3px',
  },
  compIcon: {
    fontSize: '9px',
  },
  componentsList: {
    display: 'flex',
    flexDirection: 'column',
    gap: '1px',
  },
  componentItem: {
    display: 'flex',
    alignItems: 'center',
    gap: '4px',
    fontSize: '8px',
    color: theme.colors.text,
  },
  componentIcon: {
    fontSize: '9px',
  },
  componentText: {
    lineHeight: 1.2,
  },
  examplesContainer: {
    display: 'flex',
    flexDirection: 'column',
    gap: '3px',
    flex: 1,
  },
  correctBox: {
    padding: '4px 5px',
    backgroundColor: '#dcfce7',
    borderRadius: '3px',
    borderLeft: `2px solid ${theme.colors.success}`,
  },
  incorrectBox: {
    padding: '4px 5px',
    backgroundColor: '#fee2e2',
    borderRadius: '3px',
    borderLeft: `2px solid ${theme.colors.error}`,
  },
  correctLabel: {
    display: 'flex',
    alignItems: 'center',
    gap: '3px',
    fontSize: '8px',
    fontWeight: 700,
    color: theme.colors.success,
    marginBottom: '2px',
  },
  incorrectLabel: {
    display: 'flex',
    alignItems: 'center',
    gap: '3px',
    fontSize: '8px',
    fontWeight: 700,
    color: theme.colors.error,
    marginBottom: '2px',
  },
  checkIcon: {
    fontSize: '10px',
  },
  xIcon: {
    fontSize: '10px',
  },
  exampleText: {
    fontSize: '7px',
    color: theme.colors.text,
    lineHeight: 1.25,
    margin: 0,
    fontStyle: 'italic',
  },
  noteText: {
    fontSize: '7px',
    color: theme.colors.error,
    margin: '2px 0 0 0',
    lineHeight: 1.2,
    display: 'flex',
    alignItems: 'center',
    gap: '2px',
  },
  noteIcon: {
    fontSize: '8px',
  },
  keyInsightBar: {
    backgroundColor: theme.colors.secondary,
    padding: '6px 16px',
    marginTop: '4px',
    marginLeft: '-48px',
    marginRight: '-48px',
    display: 'flex',
    alignItems: 'center',
    justifyContent: 'center',
    gap: '8px',
  },
  insightIcon: {
    fontSize: '14px',
  },
  keyInsightText: {
    fontSize: '10px',
    color: 'white',
    fontWeight: 500,
    margin: 0,
    textAlign: 'center',
  }
}
