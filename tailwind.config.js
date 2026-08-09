/** @type {import('tailwindcss').Config} */
module.exports = {
  // Escaneamos las plantillas Django (incluidas las de Cotton) para generar solo el CSS usado.
  content: [
    './templates/**/*.html',
    './applications/**/templates/**/*.html',
    './applications/**/*.py',
  ],
  // El sitio ya usa Bootstrap 5 en el resto de páginas: desactivamos el "preflight"
  // (reset global) de Tailwind para que ambos frameworks convivan sin pisarse estilos.
  corePlugins: {
    preflight: false,
  },
  theme: {
    extend: {
      colors: {
        // Paleta de marca: ocean/emerald/ink/sand. Sin amarillo/dorado a propósito
        // (no vuelvas a añadir "gold" aquí salvo que te lo pidan explícitamente).
        nica: {
          ocean: '#0b4f6c',
          emerald: '#198754',
          ink: '#0f172a',
          sand: '#f8f5ef',
        },
      },
      fontFamily: {
        heading: ['Poppins', 'sans-serif'],
        body: ['Raleway', 'sans-serif'],
      },
      boxShadow: {
        soft: '0 18px 45px rgba(15, 23, 42, 0.08)',
        lift: '0 24px 60px rgba(15, 23, 42, 0.16)',
      },
      borderRadius: {
        xl2: '1.25rem',
      },
    },
  },
  plugins: [],
}
