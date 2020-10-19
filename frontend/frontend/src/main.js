import Vue from 'vue';
import App from './App.vue'
import store from './store.js'
import router from './router.js'

Vue.config.productionTip = false;
Vue.config.ignoredElements = ['ion-icon'];

new Vue({
  router,
  store,
  render: h => h(App),
}).$mount('#app')