import Vue from 'vue'
import Router from 'vue-router'
import Login from '@/components/auth/Login'
import Home from '@/components/Home'
import Details from '../components/Details';
import Settings from '../components/Settings';

Vue.use(Router)

export default new Router({
  mode: "history",
  routes: [
    {
      path: '/',
      name: 'Home',
      component: Home
    },
    {
      path: '/login',
      name: 'Login',
      component: Login
    },
    {
      path: '/item-details/:id',
      name: 'Details',
      props: true,
      component: () =>
        import("../components/Details.vue")
    },
    {
      path: '/settings',
      name: 'Settings',
      component: Settings
    }
  ]
})
