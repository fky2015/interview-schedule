<template>
  <v-navigation-drawer v-model="drawer" app>
    <!-- <v-list dense>
      <v-list-item>
        <v-list-item-action>
          <v-icon>home</v-icon>
        </v-list-item-action>
        <v-list-item-content>
          <v-list-item-title>用户信息</v-list-item-title>
        </v-list-item-content>
      </v-list-item>
      <v-list-item>
        <v-list-item-action>
          <v-icon>contact_mail</v-icon>
        </v-list-item-action>
        <v-list-item-content>
          <v-list-item-title>社团</v-list-item-title>
        </v-list-item-content>
      </v-list-item>
    </v-list> -->

    <Interview v-for="(d, index) in data" :key="index" :data="d" />
    <router-link to="/home"> test</router-link>
    <router-link to="/about"> test</router-link>
    <router-link to="/about/2"> test</router-link>
    <router-link to="/about/afadsfd"> test</router-link>
    <router-link to="/about/.sdfa.fd"> test</router-link>
  </v-navigation-drawer>
</template>

<script>
import Interview from "./Sider/Interview.vue";
export default {
  components: {
    Interview
  },
  data: () => ({
    drawer: true,
    data: [
      {
        url: "http://127.0.0.1:8002/api-admin/interview/9/",
        pk: 9,
        title: "春招",
        edit_finish: false,
        is_public: false,
        InterviewTimeline: [
          {
            url: "http://127.0.0.1:8002/api-admin/interviewTimeline/7/",
            pk: 7,
            interview: "http://127.0.0.1:8002/api-admin/interview/9/",
            location: "教室001"
          }
        ]
      },
      {
        url: "http://127.0.0.1:8002/api-admin/interview/10/",
        pk: 10,
        title: "秋招-第二场",
        edit_finish: false,
        is_public: false,
        InterviewTimeline: [
          {
            url: "http://127.0.0.1:8002/api-admin/interviewTimeline/7/",
            pk: 7,
            interview: "http://127.0.0.1:8002/api-admin/interview/9/",
            location: "教室301"
          }
        ]
      }
    ]
  })
};
</script>

<style></style>
