import { createApp } from 'vue'
import App from './App.vue'
import router from './router'

const app = createApp(App)
app.use(router) // Tells Vue to use our router configuration
app.mount('#app')