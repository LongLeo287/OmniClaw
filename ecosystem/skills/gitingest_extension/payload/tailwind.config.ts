import type { Config } from 'tailwindcss'

export default {
  content: ["assets/**", "entrypoints/**", "components/**"],
  theme: {
    extend: {
      colors: {
        'custom-bg': '#fff4da',
        'custom-button': '#ffc480',
      },
      transitionProperty: {
        'spacing': 'margin, padding',
      },
    },
  },
  plugins: [],
} satisfies Config

