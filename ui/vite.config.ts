import { fileURLToPath, URL } from 'url' // from 'node:url' // Node >= 14.18.0
import { defineConfig } from 'vite'
import vue from '@vitejs/plugin-vue'
import Components from 'unplugin-vue-components/vite'
import AutoImport from 'unplugin-auto-import/vite'
import Icons from 'unplugin-icons/vite'

// https://vitejs.dev/config/
export default defineConfig({
  plugins: [
    vue(),
    Components({
      dts: true, // default: `true` if package typescript is installed
      dirs: ['src/components'],
    }),
    // Auto import APIs on-demand
    AutoImport({
      imports: [
        'vue',
        'vue-router',
        'vue-i18n',
        // 'vue/macros',
        '@vueuse/head',
        '@vueuse/core',
      ],
      dts: true, // or a custom path
     }),
     // Icons as components on-demand universally
     Icons({ /* options */ }),
  ],
  resolve: {
    alias: {
      '@': fileURLToPath(new URL('./src', import.meta.url))
    }
  }
})
