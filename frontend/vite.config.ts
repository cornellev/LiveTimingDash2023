import { defineConfig } from 'vite'
import react from '@vitejs/plugin-react'

export default defineConfig({
  plugins: [react()],
  base: './',
  optimizeDeps: {
    include: ['react', 'react-dom'], // Force Vite to pre-bundle them as ESM
  },
  build: {
    commonjsOptions: {
      transformMixedEsModules: true, // Ensures compatibility with mixed module formats
    }
  }
})
