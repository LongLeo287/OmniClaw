import { defineConfig } from 'vite';
import tailwindcss from '@tailwindcss/vite';

export default defineConfig({
    base: './',
    plugins: [
        tailwindcss(),
    ],
    server: {
        proxy: {
            '/api': {
                target: 'https://api.muapi.ai',
                changeOrigin: true,
                secure: false
            }
        }
    }
});
