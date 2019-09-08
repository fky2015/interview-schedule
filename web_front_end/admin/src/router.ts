/*
 * @Author: Feng Kaiyu
 * @LastEditors: Feng Kaiyu
 */
import Vue from "vue";
import Router from "vue-router";
import Home from "./views/Home.vue";

Vue.use(Router);

export default new Router({
  routes: [
    {
      path: "/",
      name: "home",
      component: Home
    },
    {
      path: "/interview/:index",
      name: "interview",
      component: () =>
        import(/* webpackChunkName: "interview" */"./components/main/Interview.vue")
    },
    {
      path: "/interview/:index/timeline/:inner_index",
      name: "interview-timeline",
      component: () =>
        import(/* webpackChunkName: "interview-timeline" */"./components/main/InterviewTimeline.vue")
    }, 
    {
      path: "/membership",
      name: "membership",
      component: () =>
        import(/* webpackChunkName: "membership" */"./components/main/Membership.vue")
    }, 
    {
      path: "/members",
      name: "members",
      component: () =>
        import(/* webpackChunkName: "member" */"@/views/Members.vue")
    },
    {
      path: "/applicants",
      name: "applicants",
      component: () =>
        import(/* webpackChunkName: "applicants" */"@/views/Applicants.vue")
    },
    {
      path: "/login",
      name: "login",
      component: () =>
        import(/* webpackChunkName: "login" */"./views/login.vue")
    }
  ]
});
