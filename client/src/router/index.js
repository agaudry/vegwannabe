import Vue from 'vue'
import VueRouter from 'vue-router'
import Home from '../components/Home.vue'
import Foods from '../components/Foods.vue'
import About from '../components/About.vue'
import Login from '../components/Login.vue'

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
    },
    {
      path: '/about',
      name: 'about',
      component: About,
    },
    {
      path: '/login',
      name: 'login',
      component: Login,
    }
  ],
});

export default router
