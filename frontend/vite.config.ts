import { defineConfig } from 'vite';

export default defineConfig({
  root: '.', // Ensure it looks at the correct directory
  build: {
    outDir: 'dist',
    rollupOptions: {
      input: 'public/index.html', // Explicitly set the input path
    }
  }
});
