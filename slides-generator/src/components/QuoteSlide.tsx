import React from 'react'
import { SlideBase } from './SlideBase'
import { theme } from '../theme'
import type { SlideContent } from '../slideContent'

interface QuoteSlideProps {
  content: SlideContent
  slideNumber: number
  totalSlides: number
}

export const QuoteSlide: React.FC<QuoteSlideProps> = ({ 
  content, 
  slideNumber, 
  totalSlides 
}) => {
  const quote = content.quote
  const bodyItems = Array.isArray(content.body) ? content.body : content.body ? [content.body] : []
  
  return (
    <SlideBase slideNumber={slideNumber} totalSlides={totalSlides} footer={content.footer}>
      <div style={styles.titleBar}>
        <h1 style={styles.title}>{content.title}</h1>
      </div>
      
      <div style={styles.quoteContainer}>
        {quote && (
          <div style={styles.quoteBlock}>
            <div style={styles.quoteMark}>"</div>
            <blockquote style={styles.quoteText}>
              {quote.text}
            </blockquote>
            <div style={styles.attribution}>
              <span style={styles.author}>— {quote.author}</span>
              {quote.source && (
                <span style={styles.source}>, {quote.source}</span>
              )}
            </div>
          </div>
        )}
        
        {bodyItems.length > 0 && (
          <div style={styles.bodyContainer}>
            {bodyItems.map((item, idx) => (
              <p key={idx} style={styles.bodyText}>{item}</p>
            ))}
          </div>
        )}
      </div>
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
    fontSize: '24px',
    fontWeight: 700,
    color: theme.colors.secondary,
    fontFamily: theme.typography.fontFamily.heading,
    margin: 0,
    lineHeight: 1.3,
  },
  quoteContainer: {
    flex: 1,
    display: 'flex',
    flexDirection: 'column',
    justifyContent: 'center',
    alignItems: 'center',
    padding: '0 40px',
  },
  quoteBlock: {
    textAlign: 'center',
    maxWidth: '700px',
  },
  quoteMark: {
    fontSize: '72px',
    fontFamily: theme.typography.fontFamily.heading,
    color: theme.colors.primary,
    opacity: 0.3,
    lineHeight: 0.5,
    marginBottom: '8px',
  },
  quoteText: {
    fontSize: '28px',
    fontWeight: 600,
    color: theme.colors.secondary,
    fontFamily: theme.typography.fontFamily.heading,
    fontStyle: 'italic',
    lineHeight: 1.4,
    margin: 0,
  },
  attribution: {
    marginTop: '24px',
    fontSize: '16px',
    color: theme.colors.textLight,
  },
  author: {
    fontWeight: 600,
    color: theme.colors.primary,
  },
  source: {
    fontStyle: 'italic',
  },
  bodyContainer: {
    marginTop: '32px',
    padding: '20px 24px',
    backgroundColor: theme.colors.lightGray,
    borderRadius: '4px',
    maxWidth: '700px',
  },
  bodyText: {
    fontSize: '14px',
    color: theme.colors.text,
    fontFamily: theme.typography.fontFamily.body,
    lineHeight: 1.6,
    margin: 0,
  }
}
