import React from 'react'
import ReactDOM from 'react-dom/client'
import App from './App'
import { cssVariables } from './theme'

// Inject CSS variables and global styles
const style = document.createElement('style')
style.textContent = `
  ${cssVariables}
  
  * {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
  }
  
  body {
    font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
    -webkit-font-smoothing: antialiased;
    -moz-osx-font-smoothing: grayscale;
  }
  
  button:hover {
    opacity: 0.9;
  }
  
  button:active {
    transform: scale(0.98);
  }
`
document.head.appendChild(style)

ReactDOM.createRoot(document.getElementById('root')!).render(
  <React.StrictMode>
    <App />
  </React.StrictMode>,
)
