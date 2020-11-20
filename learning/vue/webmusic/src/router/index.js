import Vue from "Vue"
import createRouter from 'vue-router'
// import createWebHashHistory from 'vue-router'

Vue.useCssModule(createRouter)

import Main from '@/views/Main.vue'

const routes = [{
    path: '/',
    component: Main
}]

const router = createRouter({
    // history: createWebHashHistory()
    routes
})

export default router

// import Vue from 'vue'
// import VueRouter from 'vue-router'
// import Main from '@/views/Main.vue'

// Vue.useCssModule(VueRouter)

// const routes = [{
//     path: '/',
//     component: Main
// }]

// const router = new VueRouter({
//     // history: createWebHashHistory()
//     routes
// })

// export default router