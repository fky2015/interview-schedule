import Vue from "vue";
import App from "./App.vue";
import router from "./router";
import store from "./store";
import vuetify from "./plugins/vuetify";
import axios from "axios";
import VueAxios from 'vue-axios';

Vue.config.productionTip = false;
// Vue.prototype.$http = axios;
Vue.use(VueAxios, axios);

// Add a request interceptor
axios.interceptors.request.use(function (config) {
  // Do something before request is sent
  console.group(`(send)[${config.method}] ${config.url}`)
  console.info(config)
  console.groupEnd()
  return config;
}, function (error) {
  // Do something with request error
  return Promise.reject(error);
});


axios.interceptors.response.use(
  function (response) {
    // Do something with response data
    console.group(`(get)[${response.config.method}] ${response.config.url}`)
    console.info(response.data)
    console.groupEnd()
    return response
  },
  function (error) {
    // Do something with response error
    if (error.response && error.response.config && error.response.data) {
      console.group(`(getErr)[${error.response.config.method}] ${error.response.config.url}`)
      console.info(error.response.data)
      console.groupEnd()
    }

    if (error.response && error.response.statusText === "Unauthorized") {
      // do somethings
      window.open("/accounts/login/", "", "", true)
    }
    return Promise.reject(error);
  }
);

new Vue({
  router,
  store,
  vuetify,
  render: h => h(App)
}).$mount("#app");
