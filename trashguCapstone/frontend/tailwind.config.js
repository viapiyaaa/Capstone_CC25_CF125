// File: frontend/tailwind.config.js

module.exports = {
  content: [
    './src/**/*.html',   // Memantau semua file HTML di dalam src
    './src/**/*.js',     // Memantau semua file JavaScript di dalam src
  ],
  theme: {
    extend: {
        fontFamily: {
          poppins: ['Poppins'],
        },
        colors: { 
            'custom-green': '#3F7D58',
            'custom-green-darker': '#326748',
            'text-customText': '#414141',
            'hero-bg': '#EFEFEF', 
            'section-bg': '#F5F7FA', 
            'footer-bg': '#EFEFEF', 
          }
    },
  },
  plugins: [],
};
