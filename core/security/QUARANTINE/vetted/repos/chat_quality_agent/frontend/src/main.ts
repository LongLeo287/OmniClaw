import { createApp } from 'vue'
import { createPinia } from 'pinia'
import vuetify from './plugins/vuetify'
import i18n from './i18n'
import router from './router'
import App from './App.vue'

const app = createApp(App)
app.use(createPinia())
app.use(vuetify)
app.use(i18n)
app.use(router)
app.mount('#app')
