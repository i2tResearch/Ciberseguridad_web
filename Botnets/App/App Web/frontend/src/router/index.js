import Vue from 'vue'
import VueRouter from 'vue-router'
import Login from './../pages/Login/Home'
import Dashboard from './../pages/Dashboard/Dash'
import About from './../pages/About/About'
import Store from './../store/index.js'


Vue.use(VueRouter)

  const routes = [
    { path: '*', component: Login },
    { path: '/', name: "Login", component: Login },
    { path: '/login', component: Login },
    { path: '/Dashboard', name: "Dash", component: Dashboard,
      beforeEnter: (to, from, next) => {
        if (Store.state.authenticated) {
          next();
        } else {
          next('');
        }
      }
    },
    { path: '/about', name: "About", component: About,
    beforeEnter: (to, from, next) => {
      if (Store.state.authenticated) {
        next();
      } else {
        next('');
      }
    }
  }
]

const router = new VueRouter({
  routes
})

export default router
