import Vue from 'vue'
import Router from 'vue-router'
import HelloWorld from "@/components/HelloWorld.vue"
import Test from "@/components/test.vue"

Vue.use(Router)

export default new Router({
    routes: [{
            path: '/',
            name: 'HelloWorld',
            component: HelloWorld
        },
        {
            path: '/test',
            name: 'test',
            component: Test
        }
    ]
})