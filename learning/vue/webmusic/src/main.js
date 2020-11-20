import { createApp } from 'vue'
import App from './App.vue'
import router from './router'
import store from './store'
import '@/style.scss'

createApp(App).use(store).use(router).mount('#app')


// import Vue from 'vue'
// import App from './App.vue'
// import router from './router'
// import store from './store'

// Vue.config.productionTip = false

// import '@/style.scss'

// new Vue({
//     router,
//     store,
//     render: h => h(App)
// }).$mount("#app")

// new { createApp }({
//     router,
//     store,
//     render: h => h(App)
// }).$mount("#app")