import Vue from "vue";
import "./plugins/vuetify";
import App from "./App.vue";
import router from "./router";
import store from "./store";
import 'material-design-icons-iconfont/dist/material-design-icons.css'
Vue.config.productionTip = false;

new Vue({
  iconfont: 'fa4',// 'md' || 'mdi' || 'fa' || 'fa4'
  router,
  store,
  render: h => h(App)
}).$mount("#app");
