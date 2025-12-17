import React from 'react'
import { SlideBase } from './SlideBase'
import { theme } from '../theme'
import type { SlideContent } from '../slideContent'

interface TitleSlideProps {
  content: SlideContent
  slideNumber: number
  totalSlides: number
}

export const TitleSlide: React.FC<TitleSlideProps> = ({ 
  content, 
  slideNumber, 
  totalSlides 
}) => {
  return (
    <SlideBase slideNumber={slideNumber} totalSlides={totalSlides} footer={content.footer}>
      <div style={styles.container}>
        <div style={styles.accentBar} />
        <h1 style={styles.title}>{content.title}</h1>
        {content.subtitle && (
          <h2 style={styles.subtitle}>{content.subtitle}</h2>
        )}
        <div style={styles.divider} />
      </div>
    </SlideBase>
  )
}

const styles: Record<string, React.CSSProperties> = {
  container: {
    display: 'flex',
    flexDirection: 'column',
    justifyContent: 'center',
    alignItems: 'center',
    height: '100%',
    textAlign: 'center',
  },
  accentBar: {
    width: '80px',
    height: '4px',
    backgroundColor: theme.colors.primary,
    marginBottom: '32px',
  },
  title: {
    fontSize: '40px',
    fontWeight: 700,
    color: theme.colors.secondary,
    fontFamily: theme.typography.fontFamily.heading,
    margin: 0,
    marginBottom: '16px',
    lineHeight: 1.2,
  },
  subtitle: {
    fontSize: '20px',
    fontWeight: 400,
    color: theme.colors.textLight,
    fontFamily: theme.typography.fontFamily.body,
    margin: 0,
    marginTop: '8px',
  },
  divider: {
    width: '120px',
    height: '2px',
    backgroundColor: theme.colors.lightGray,
    marginTop: '40px',
  }
}
