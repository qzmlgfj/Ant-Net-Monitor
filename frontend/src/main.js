import { createApp } from 'vue'
import App from './App.vue'
import router from './router'
import store from './utils/store'
import 'vfonts/Lato.css'
import 'vfonts/FiraCode.css'

createApp(App)
    .use(router)
    .use(store)
    .mount('#app')
