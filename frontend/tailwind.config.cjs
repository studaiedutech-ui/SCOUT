/**** Tailwind CSS Config ****/
module.exports = {
  content: [
    './index.html',
    './src/**/*.{js,ts,jsx,tsx}'
  ],
  theme: {
    extend: {
      colors: {
        primary: '#2563EB',
        secondary: '#F59E0B',
        success: '#10B981',
        warning: '#F59E0B',
        error: '#EF4444',
        neutral: '#6B7280'
      }
    }
  },
  plugins: []
};
