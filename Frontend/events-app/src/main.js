import Vue from 'vue'
import App from './App.vue'
import router from './router'
import './../node_modules/bulma/css/bulma.css'
import VueResource from 'vue-resource'
import store from './store'
import AsyncComputed from 'vue-async-computed'
import VModal from 'vue-js-modal'

Vue.use(VueResource);
Vue.use(AsyncComputed)
Vue.use(VModal)



Vue.config.productionTip = false

new Vue({
  router,
  store,
  render: h => h(App)
}).$mount('#app')
