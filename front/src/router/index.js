import Vue from 'vue'
import VueRouter from 'vue-router'
import store from "@/store";

Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'Manage',
    component: () => import('../views/Manage.vue'),
    redirect: '/home',
    children:[
      {path: 'home', name: 'Home', component: () => import('../components/Home')},
      {path: 'interview', name: 'Interview', component: () => import('../components/Interview')},
      {path: '/booking', name: 'Booking', component: () => import('../components/Booking')},
      {path: '/results', name: 'Results', component: () => import('../components/Results')},
      {
        path: '/question',
        name: 'Question',
        component: () => import('../components/Question.vue')
      },
      {
        path: '/arrangement',
        name: 'Arrangement',
        component: () => import('../components/Arrangement.vue')
      },
      {
        path: '/businessRank',
        name: 'businessRank',
        component: () => import('../components/businessRank.vue')
      },
      {
        path: '/ReviewChange',
        name: 'ReviewChange',
        component: () => import('../components/ReviewChange.vue')
      },
      {
        path: '/NewUser',
        name: 'NewUser',
        component: () => import('../components/NewUser.vue')
      },
      {
        path: '/UserActivity',
        name: 'UserActivity',
        component: () => import('../components/UserActivity.vue')
      },
      {
        path: '/businessType',
        name: 'businessType',
        component: () => import('../components/businessType.vue')
      },
      {
        path: '/WordCloud',
        name: 'WordCloud',
        component: () => import('../components/WordCloud.vue')
      },
      {
        path: '/areaRank',
        name: 'areaRank',
        component: () => import('../components/areaRank.vue')
      },
    ]
  },
  {
    path: '/login',
    name: 'Login',
    component: () => import('../views/Login.vue')
  },
  {
    path: '/register',
    name: 'Register',
    component: () => import('../views/Register.vue')
  },
  {
    path: '/user',
    name: 'User',
    component: () => import('../views/User.vue')
    // children: [
    //
    // ]
  },
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

// 路由守卫
router.beforeEach((to, from, next) => {
  localStorage.setItem("currentPathName", to.name)  // 设置当前的路由名称，为了在Header组件中去使用
  store.commit("setPath")  // 触发store的数据更新
  next()  // 放行路由
})

export default router
