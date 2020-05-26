import Vue from 'vue'
import VueRouter from 'vue-router'
import Home from '../components/Home.vue'
import Foods from '../components/Foods.vue'

Vue.use(VueRouter)

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes: [
    {
      path: '/',
      name: 'home',
      component: Home,
    },
    {
      path: '/display_foods',
      name: 'foods',
      component: Foods,
    }
  ],
});

export default router
