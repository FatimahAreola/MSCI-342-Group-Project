import Vue from 'vue';
import App from './App.vue';
import store from './store.js';
import router from './router.js';
// notification library
import Notifications from 'vue-notification';
Vue.config.productionTip = false;
Vue.config.ignoredElements = ['ion-icon'];

Vue.use(Notifications)

new Vue({
  router,
  store,
  render: h => h(App),
}).$mount('#app')