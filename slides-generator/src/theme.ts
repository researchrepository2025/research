// McKinsey/BCG-inspired design tokens
export const theme = {
  colors: {
    primary: '#005eb8',      // McKinsey blue
    secondary: '#222222',    // Dark gray/black
    background: '#ffffff',   // White
    lightGray: '#f5f5f5',    // Light gray backgrounds
    mediumGray: '#a2aaad',   // Medium gray
    accent: '#0a3d62',       // Darker blue for emphasis
    success: '#2d8a5e',      // Green for correct examples
    error: '#c0392b',        // Red for incorrect examples
    text: '#333333',         // Body text
    textLight: '#666666',    // Secondary text
  },
  
  typography: {
    fontFamily: {
      heading: '"Georgia", serif',
      body: '"Arial", "Helvetica Neue", sans-serif',
    },
    fontSize: {
      title: '32pt',
      subtitle: '24pt',
      heading: '20pt',
      subheading: '16pt',
      body: '14pt',
      small: '12pt',
      footnote: '10pt',
    },
    fontWeight: {
      regular: 400,
      medium: 500,
      bold: 700,
    },
  },
  
  spacing: {
    margin: '1in',        // 1-inch margins
    padding: {
      small: '8px',
      medium: '16px',
      large: '24px',
      xlarge: '32px',
    },
    gap: {
      small: '8px',
      medium: '16px',
      large: '24px',
    },
  },
  
  slide: {
    width: 960,           // 10 inches at 96 DPI
    height: 540,          // 5.625 inches at 96 DPI (16:9)
    aspectRatio: '16/9',
  },
}

// CSS variables for easy use
export const cssVariables = `
  :root {
    --color-primary: ${theme.colors.primary};
    --color-secondary: ${theme.colors.secondary};
    --color-background: ${theme.colors.background};
    --color-light-gray: ${theme.colors.lightGray};
    --color-medium-gray: ${theme.colors.mediumGray};
    --color-accent: ${theme.colors.accent};
    --color-success: ${theme.colors.success};
    --color-error: ${theme.colors.error};
    --color-text: ${theme.colors.text};
    --color-text-light: ${theme.colors.textLight};
    
    --font-heading: ${theme.typography.fontFamily.heading};
    --font-body: ${theme.typography.fontFamily.body};
    
    --slide-width: ${theme.slide.width}px;
    --slide-height: ${theme.slide.height}px;
  }
`
