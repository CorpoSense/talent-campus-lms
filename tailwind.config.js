// tailwind.config.js
/** @type {import('tailwindcss').Config} */
export default {
  content: [
    "./index.html",
    "./src/*.{js,ts,jsx,tsx}",
    "./src/components/*.{js,ts,jsx,tsx}",
    "./src/pages/*.{js,ts,jsx,tsx}",
    "./public/*.svg"
  ],
  theme: {
    extend: {
      colors: {
        'blue-custom': '#007BFF',
        'green-custom': '#28A745'
      },
      fontFamily: {
        sans: ['Lato', 'sans-serif'],
       'pt-serif': ['PT Serif', 'serif'],

      },
      backgroundImage: {
        'gradient-text': 'linear-gradient(90deg, #007BFF 0%, #28A745 30%)'
      }
    },
    screens: {
      'xxs': '340px',
      'xs': '430px',
      'sm': '640px',
      'b-sm': '730px',
      'md': '768px',
      'lg': '1024px',
      'xl': '1280px',
      '2xl': '1536px',
    },
  },
  plugins: [
    function ({ addUtilities }) {
      addUtilities(
        {
          '.text-gradient': {
            background: 'linear-gradient(80deg, #007BFF 0%, #28A745 30%)',
            '-webkit-background-clip': 'text',
            '-webkit-text-fill-color': 'transparent',
          }
        },
        ['responsive', 'hover']
      )
    }
  ],
}
