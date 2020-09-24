import Vue from 'vue'
import VueRouter from 'vue-router'

const Home = () => import('../views/Home');
const About = () => import('../views/About');
const Login = () => import('../views/Login');
const HomePage = () => import('../views/Homepage');
const CompletedForms = () => import('../components/FormFeatures/CompletedForms');
const PendingForms = () => import('../components/FormFeatures/Sales/PendingForms');
const ConcernedForms = () => import('../components/FormFeatures/ConcernedForms');
const CreateForm = () => import('../components/FormFeatures/Sales/CreateForm');
const resetPassword = () => import('../components/GeneralFeatures/ResetPsw');
const resetOtherPassword = () => import('../components/GeneralFeatures/ResetOtherPsw');
const CreateAccount = () => import('../components/GeneralFeatures/CreateAccount');
const DeleteAccount = () => import('../components/GeneralFeatures/DeleteAccount');
const UncompletedForms = () => import('../components/FormFeatures/Buyer/UncompletedForms');

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
          path: 'uncompleted_forms',
          name: 'Uncompleted Forms',
          component: UncompletedForms
        },
        {
          path: 'completed_forms',
          name: 'Completed Forms',
          component: CompletedForms
        },
        {
          path: 'pending_forms',
          name: 'Pending Forms',
          component: PendingForms
        },
        {
          path: 'concerned_forms',
          name: 'Concerned Forms',
          component: ConcernedForms
        },
        {
          path: 'create_form',
          name: 'Create Form',
          component: CreateForm
        },
        {
          path: 'reset_my_password',
          name: 'Reset My Password',
          component: resetPassword
        },
        {
          path: 'reset_other_password',
          name: 'Reset Other Password',
          component: resetOtherPassword
        },
        {
          path: 'create_account',
          name: 'Create Account',
          component: CreateAccount
        },
        {
          path: 'delete_account',
          name: 'Delete Account',
          component: DeleteAccount
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
