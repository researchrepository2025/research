import React from 'react'
import { SlideBase } from './SlideBase'
import { theme } from '../theme'
import type { SlideContent } from '../slideContent'

interface TableSlideProps {
  content: SlideContent
  slideNumber: number
  totalSlides: number
}

export const TableSlide: React.FC<TableSlideProps> = ({ 
  content, 
  slideNumber, 
  totalSlides 
}) => {
  const table = content.table
  
  if (!table) return null
  
  return (
    <SlideBase slideNumber={slideNumber} totalSlides={totalSlides} footer={content.footer}>
      <div style={styles.titleBar}>
        <h1 style={styles.title}>{content.title}</h1>
      </div>
      
      <div style={styles.tableContainer}>
        <table style={styles.table}>
          <thead>
            <tr>
              {table.headers.map((header, idx) => (
                <th key={idx} style={{
                  ...styles.headerCell,
                  backgroundColor: idx === 0 ? theme.colors.secondary : theme.colors.primary,
                }}>
                  {header}
                </th>
              ))}
            </tr>
          </thead>
          <tbody>
            {table.rows.map((row, rowIdx) => (
              <tr key={rowIdx}>
                {row.map((cell, cellIdx) => (
                  <td key={cellIdx} style={{
                    ...styles.cell,
                    fontWeight: cellIdx === 0 ? 600 : 400,
                    backgroundColor: cellIdx === 0 ? theme.colors.lightGray : 'white',
                  }}>
                    {cell}
                  </td>
                ))}
              </tr>
            ))}
          </tbody>
        </table>
      </div>
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
    fontSize: '20px',
    fontWeight: 700,
    color: theme.colors.secondary,
    fontFamily: theme.typography.fontFamily.heading,
    margin: 0,
    lineHeight: 1.3,
  },
  tableContainer: {
    flex: 1,
    display: 'flex',
    alignItems: 'flex-start',
  },
  table: {
    width: '100%',
    borderCollapse: 'collapse',
    fontSize: '13px',
    fontFamily: theme.typography.fontFamily.body,
  },
  headerCell: {
    padding: '12px 16px',
    color: 'white',
    fontWeight: 700,
    textAlign: 'left',
    fontSize: '13px',
    letterSpacing: '0.3px',
  },
  cell: {
    padding: '12px 16px',
    borderBottom: `1px solid ${theme.colors.lightGray}`,
    color: theme.colors.text,
    lineHeight: 1.4,
    fontSize: '13px',
  }
}
