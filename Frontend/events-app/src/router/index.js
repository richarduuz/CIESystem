import Vue from 'vue'
import VueRouter from 'vue-router'

const Home = () => import('../views/Home');
const About = () => import('../views/About');
const Login = () => import('../views/Login');
const HomePage = () => import('../views/Homepage');
const FormHistory = () => import('../components/FormFeatures/FormHistory');
const CreateForm = () => import('../components/FormFeatures/CreateForm');

Vue.use(VueRouter);

  const routes = [
  {
    path: '/home',
    name: 'Home',
    component: Home
  },
  {
      path: '',
      redirect: '/home'
  },
  {
    path: '/about',
    name: 'About',
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: About
  },
  {
      path: '/login',
      name: 'Login',
      component: Login
  },
  {
      path: '/homepage/:username',
      name: 'HomePage',
      component: HomePage,
      children: [
        {
          path: 'form_history',
          name: 'Form_History',
          component: FormHistory
        },
        {
          path: 'create_form',
          name: 'Create_Form',
          component: CreateForm
        }
      ]
  }
];

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
});

export default router
