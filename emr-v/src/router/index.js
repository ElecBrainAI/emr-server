import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'
import LoginView from '../views/LoginView.vue'
import SignUpView from "../views/SignUpView.vue";
import PatientView from "../views/PatientView.vue";
import ReceptionView from "../views/ReceptionView.vue";
import ReceiveView from "../views/ReceiveView.vue";
import LoinView2 from "../views/LoginView2.vue"
const routes = [
  {
    path: '/',
    name: 'home2',
    component: LoinView2
  },
  {
    path: '/move',
    name: 'home',
    component: HomeView
  },
  {
    path: '/login',
    name: 'login',
    component: LoginView
  },
  {
    path: '/signup',
    name: 'signup',
    component: SignUpView
  },
  {
    path: '/patient',
    name: 'patient',
    component: PatientView
  },
  {
    path: '/reception',
    name: 'reception',
    component: ReceptionView
  },
  {
    path: '/receive',
    name: 'receive',
    component: ReceiveView
  }
]

const router = createRouter({
  history: createWebHistory(),
  routes
})

export default router