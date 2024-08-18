import { createRouter, createWebHistory } from 'vue-router'
import NProgress from 'nprogress'
// import AboutView from '@/views/AboutView.vue'
import NotFound from "@/views/NotFound.vue"
import NetworkError from "@/views/NetworkError.vue"
import Home from '@/views/Home.vue'
import Signin from '@/views/Signin.vue'


const About = () => import(/* webpackChunkName: "about", */ '@/views/About.vue')

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  scrollBehavior(_to, _from, savedPosition) {
      return savedPosition || { top: 0}
  },
  routes: [
    {
      path: '/',
      name: 'home',
      component: Home
    },
    {
      path: '/about',
      name: 'about',
      component: About
    },
    {
      path: '/login',
      name: 'login',
      component: Signin
    },
    {
      path: "/:catchAll(.*)",
      name: "NotFound",
      component: NotFound,
    },
    {
      path: "/404/:resource",
      name: "404Resource",
      component: NotFound,
      props: true,
    },
    {
      path: "/network-error",
      name: "NetworkError",
      component: NetworkError,
    },
  ],
})

router.beforeEach((to: any, from: any) => {
  NProgress.start()

  const notAuthorized = true
  if (to.meta.requireAuth && notAuthorized){

    setTimeout(() => {
      NProgress.done()
    }, 3000)

    if (from.href){
      return false
    } else {
      return { path: '/'}
    }
  }
})

export default router
