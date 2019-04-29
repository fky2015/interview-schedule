import Vue from "vue";
import Router from "vue-router";

Vue.use(Router);

export default new Router({
  routes: [
    {
      path: "/about",
      name: "about",
      // route level code-splitting
      // this generates a separate chunk (about.[hash].js) for this route
      // which is lazy-loaded when the route is visited.
      component: () =>
        import(/* webpackChunkName: "about" */ "./views/About.vue")
    },
    {
      path: "/sign-up",
      name: "sign-up",
      component: () =>
        import(/* webpackChunkName: "about" */ "./views/SignUp.vue")
    },
    {
      path: "/sign-in",
      name: "sign-in",
      component: () =>
        import(/* webpackChunkName: "about" */ "./views/SignIn.vue")
    },
    {
      path: "/",
      name: "square",
      component: () =>
        import(/* webpackChunkName: "about" */ "./views/Square.vue")
    },
    {
      path: "/me",
      name: "me",
      component: () => import(/* webpackChunkName: "about" */ "./views/UserInfo.vue")
    }
  ]
});
