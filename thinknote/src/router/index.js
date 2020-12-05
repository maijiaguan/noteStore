import Vue from 'vue'
import Router from 'vue-router'
import Login from '@/page/Login'
import Home from '@/page/Home'
import VueCookies from 'vue-cookies'

Vue.use(Router)

const router = new Router({
  mode: 'history',
  routes: [
    {
      path: '',
      redirect: '/login'
    },
    {
      path: '/home',
      name: 'Home',
      component: Home
    },
    {
      path: '/login',
      name: 'Login',
      component: Login
    }
  ]
})

router.beforeEach((to, from, next) => {
  let login = VueCookies.get('access')
  console.log(login)
  if (to.path.includes('/login')) login ? next('/home') : next()
  if (to.path.includes('/home')) login ? next() : next('/login')
  // console.log(isLogin)
  // next('/login')
})

export default router
