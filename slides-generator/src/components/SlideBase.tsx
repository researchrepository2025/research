import React from 'react'
import { theme } from '../theme'

interface SlideBaseProps {
  children: React.ReactNode
  slideNumber: number
  totalSlides: number
  footer?: string
}

export const SlideBase: React.FC<SlideBaseProps> = ({ 
  children, 
  slideNumber, 
  totalSlides,
  footer 
}) => {
  return (
    <div style={styles.slide}>
      <div style={styles.content}>
        {children}
      </div>
      <div style={styles.footer}>
        <span style={styles.footerText}>{footer || ''}</span>
        <span style={styles.pageNumber}>{slideNumber} / {totalSlides}</span>
      </div>
    </div>
  )
}

const styles: Record<string, React.CSSProperties> = {
  slide: {
    width: '960px',
    height: '540px',
    backgroundColor: theme.colors.background,
    boxShadow: '0 4px 20px rgba(0,0,0,0.15)',
    position: 'relative',
    overflow: 'hidden',
    fontFamily: theme.typography.fontFamily.body,
    display: 'flex',
    flexDirection: 'column',
  },
  content: {
    flex: 1,
    padding: '40px 48px 24px 48px',
    display: 'flex',
    flexDirection: 'column',
  },
  footer: {
    height: '32px',
    padding: '0 48px',
    display: 'flex',
    justifyContent: 'space-between',
    alignItems: 'center',
    borderTop: `1px solid ${theme.colors.lightGray}`,
    backgroundColor: theme.colors.background,
  },
  footerText: {
    fontSize: '10px',
    color: theme.colors.textLight,
    fontFamily: theme.typography.fontFamily.body,
  },
  pageNumber: {
    fontSize: '10px',
    color: theme.colors.textLight,
    fontFamily: theme.typography.fontFamily.body,
  }
}
