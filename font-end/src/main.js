import Vue from 'vue'
import ElementUI from 'element-ui';
import 'element-ui/lib/theme-chalk/index.css';
import router from './router'
import App from './App.vue'
import axios from 'axios'
import VueAxios from 'vue-axios'

Vue.use(VueAxios, axios)
Vue.prototype.$axios = axios
Vue.config.productionTip = false
Vue.use(ElementUI);
Vue.use(router)

new Vue({
  router,
  render: h => h(App),
}).$mount('#app')
