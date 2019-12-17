import Vue from 'vue'
import Router from 'vue-router'
// import Home from '../views/Home.vue'

Vue.use(Router)

export default new Router({
    mode: 'history',
    base: process.env.BASE_URL,
    routes:[
        {
            path: '/',
            name: 'index',
            component: () => import('./views/index.vue'),
            redirect:'/first',
            children:[
                {
                    path:'/first',     // 首页
                    name:'first',
                    component: () => import('./views/first.vue'),
                },
                {
                    path:'/laptop',     // 笔记本电脑页
                    name:'laptop',
                    component: () => import('./views/laptop.vue')
                },
                {
                    path:'/desktop',    // 台式机电脑页
                    name:'desktop',
                    component: () => import('./views/desktop.vue')
                },
                {
                    path:'/peripheral',     // 外设页
                    name:'peripheral',
                    component: () => import('./views/peripheral.vue')
                },
                {
                    path:'/evalution',     // 评测中心
                    name:'evalution',
                    component: () => import('./views/evalution.vue')
                },
                {
                    path:'/service',     // 售后服务
                    name:'service',
                    component: () => import('./views/service.vue')
                },
            ]
        }
    ]
  })
  
