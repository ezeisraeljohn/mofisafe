/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
        './mofisafe_app/templates/**/*.html',
        './mofisafe_app/static/**/*.js',
        "./node_modules/flowbite/**/*.js"
  ],
  theme: {
    extend: {},
  },
  plugins: [
        require('flowbite/plugin')
  ],
}

