/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    './templates/**/*.html',
    './blog/templates/**/*.html',  // adjust if your template location is different
  ],
  theme: {
    extend: {},
  },
  plugins: [require("daisyui")],
  daisyui: {
    themes: ["cupcake"], // you can add more themes or customize them
  }
}