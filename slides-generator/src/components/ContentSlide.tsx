import React from 'react'
import { SlideBase } from './SlideBase'
import { theme } from '../theme'
import type { SlideContent } from '../slideContent'

interface ContentSlideProps {
  content: SlideContent
  slideNumber: number
  totalSlides: number
}

export const ContentSlide: React.FC<ContentSlideProps> = ({ 
  content, 
  slideNumber, 
  totalSlides 
}) => {
  const bodyItems = Array.isArray(content.body) ? content.body : content.body ? [content.body] : []
  
  return (
    <SlideBase slideNumber={slideNumber} totalSlides={totalSlides} footer={content.footer}>
      <div style={styles.titleBar}>
        <h1 style={styles.title}>{content.title}</h1>
      </div>
      <div style={styles.bodyContainer}>
        <ul style={styles.bulletList}>
          {bodyItems.map((item, idx) => (
            <li key={idx} style={styles.bulletItem}>
              <span style={styles.bulletPoint} />
              <span style={styles.bulletText}>{item}</span>
            </li>
          ))}
        </ul>
      </div>
    </SlideBase>
  )
}

const styles: Record<string, React.CSSProperties> = {
  titleBar: {
    borderBottom: `3px solid ${theme.colors.primary}`,
    paddingBottom: '16px',
    marginBottom: '32px',
  },
  title: {
    fontSize: '24px',
    fontWeight: 700,
    color: theme.colors.secondary,
    fontFamily: theme.typography.fontFamily.heading,
    margin: 0,
    lineHeight: 1.3,
  },
  bodyContainer: {
    flex: 1,
    display: 'flex',
    flexDirection: 'column',
    justifyContent: 'flex-start',
  },
  bulletList: {
    listStyle: 'none',
    padding: 0,
    margin: 0,
  },
  bulletItem: {
    display: 'flex',
    alignItems: 'flex-start',
    marginBottom: '20px',
  },
  bulletPoint: {
    width: '8px',
    height: '8px',
    borderRadius: '50%',
    backgroundColor: theme.colors.primary,
    marginTop: '8px',
    marginRight: '16px',
    flexShrink: 0,
  },
  bulletText: {
    fontSize: '18px',
    color: theme.colors.text,
    fontFamily: theme.typography.fontFamily.body,
    lineHeight: 1.5,
  }
}
