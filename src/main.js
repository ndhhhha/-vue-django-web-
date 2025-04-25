import 'element-plus/dist/index.css'
import pinia from './stores'
import { createApp } from 'vue'

import App from './App.vue'
import router from './router'

import vSlideIn from './utils/vSlideIn'

const app = createApp(App)
app.use(router)
app.use(pinia)
// 注册全局自定义指令
app.directive('v-slide-in', vSlideIn)
app.mount('#app')
