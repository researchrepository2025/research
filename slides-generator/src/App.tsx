import React, { useState } from 'react'
import { slides } from './slideContent'
import { exportToPptx } from './utils/exportToPptx'
import { DefinitionsSlide } from './components/DefinitionsSlide'
import { AlignmentSlide } from './components/AlignmentSlide'
import { theme } from './theme'

function App() {
  const [currentSlide, setCurrentSlide] = useState(0)
  const totalSlides = slides.length
  
  const handlePrevSlide = () => {
    setCurrentSlide(prev => Math.max(0, prev - 1))
  }
  
  const handleNextSlide = () => {
    setCurrentSlide(prev => Math.min(totalSlides - 1, prev + 1))
  }
  
  const handleExport = () => {
    exportToPptx(slides, {
      author: 'Corporate Strategy',
      title: 'Strategy, Goals & Tactics',
      subject: 'Corporate Strategy Framework'
    })
  }
  
  const handleKeyDown = (e: React.KeyboardEvent) => {
    if (e.key === 'ArrowRight' || e.key === ' ') {
      handleNextSlide()
    } else if (e.key === 'ArrowLeft') {
      handlePrevSlide()
    }
  }
  
  const renderSlide = () => {
    const content = slides[currentSlide]
    const props = {
      content,
      slideNumber: currentSlide + 1,
      totalSlides
    }
    
    if (content.type === 'definitions') {
      return <DefinitionsSlide {...props} />
    } else {
      return <AlignmentSlide {...props} />
    }
  }
  
  return (
    <div style={styles.app} onKeyDown={handleKeyDown} tabIndex={0}>
      <header style={styles.header}>
        <h1 style={styles.headerTitle}>Strategy Slides Preview</h1>
        <div style={styles.headerControls}>
          <span style={styles.slideCounter}>
            Slide {currentSlide + 1} of {totalSlides}
          </span>
          <button style={styles.exportButton} onClick={handleExport}>
            Export to PowerPoint
          </button>
        </div>
      </header>
      
      <main style={styles.main}>
        <div style={styles.slideContainer}>
          {renderSlide()}
        </div>
        
        <div style={styles.navigation}>
          <button 
            style={{
              ...styles.navButton,
              opacity: currentSlide === 0 ? 0.5 : 1
            }}
            onClick={handlePrevSlide}
            disabled={currentSlide === 0}
          >
            ← Previous
          </button>
          
          <div style={styles.slideInfo}>
            <span style={styles.slideTitle}>
              {currentSlide === 0 ? 'Strategy Definitions' : 'Alignment Comparison'}
            </span>
          </div>
          
          <button 
            style={{
              ...styles.navButton,
              opacity: currentSlide === totalSlides - 1 ? 0.5 : 1
            }}
            onClick={handleNextSlide}
            disabled={currentSlide === totalSlides - 1}
          >
            Next →
          </button>
        </div>
      </main>
      
      <footer style={styles.footer}>
        <p>Use arrow keys to navigate. Click "Export to PowerPoint" to download.</p>
      </footer>
    </div>
  )
}

const styles: Record<string, React.CSSProperties> = {
  app: {
    minHeight: '100vh',
    backgroundColor: '#1a1a2e',
    display: 'flex',
    flexDirection: 'column',
    outline: 'none',
  },
  header: {
    padding: '16px 32px',
    display: 'flex',
    justifyContent: 'space-between',
    alignItems: 'center',
    borderBottom: '1px solid #333',
  },
  headerTitle: {
    margin: 0,
    fontSize: '18px',
    color: '#fff',
    fontWeight: 500,
  },
  headerControls: {
    display: 'flex',
    alignItems: 'center',
    gap: '24px',
  },
  slideCounter: {
    color: '#888',
    fontSize: '14px',
  },
  exportButton: {
    padding: '10px 20px',
    backgroundColor: theme.colors.primary,
    color: '#fff',
    border: 'none',
    borderRadius: '4px',
    fontSize: '14px',
    fontWeight: 600,
    cursor: 'pointer',
    transition: 'background-color 0.2s',
  },
  main: {
    flex: 1,
    display: 'flex',
    flexDirection: 'column',
    alignItems: 'center',
    justifyContent: 'center',
    padding: '24px 40px',
  },
  slideContainer: {
    display: 'flex',
    justifyContent: 'center',
    alignItems: 'center',
  },
  navigation: {
    display: 'flex',
    alignItems: 'center',
    gap: '24px',
    marginTop: '24px',
    width: '100%',
    justifyContent: 'center',
  },
  navButton: {
    padding: '12px 24px',
    backgroundColor: 'transparent',
    color: '#fff',
    border: '1px solid #444',
    borderRadius: '4px',
    fontSize: '14px',
    cursor: 'pointer',
    transition: 'all 0.2s',
  },
  slideInfo: {
    padding: '8px 16px',
    backgroundColor: '#2d2d44',
    borderRadius: '4px',
  },
  slideTitle: {
    color: '#aaa',
    fontSize: '13px',
  },
  footer: {
    padding: '16px 32px',
    textAlign: 'center',
    borderTop: '1px solid #333',
    color: '#666',
    fontSize: '13px',
  }
}

export default App
