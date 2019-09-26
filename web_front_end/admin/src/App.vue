<template>
  <v-app id="inspire">
    <v-navigation-drawer v-model="drawer" app>
      <Sider :clubs="owned_clubs" />
    </v-navigation-drawer>

    <v-app-bar flat app color="primary" dark>
      <v-app-bar-nav-icon @click.stop="drawer = !drawer"></v-app-bar-nav-icon>
      <v-toolbar-title>社团面试管理系统</v-toolbar-title>
      <v-spacer></v-spacer>
      <v-select
        background-color="primary"
        flat
        dense
        @change="onChooseClub"
        append-icon
        hide-details
        placeholder="选择一个社团"
        v-model="club_url"
        :items="clubs"
        item-text="name"
        item-value="url"
        solo
      ></v-select>

      <v-spacer></v-spacer>
      <router-link :to="h.link" v-for="(h, idx) in headers" :key="idx">
        <v-btn text>
          {{ h.text }}
          <v-icon>mdi-{{ h.icon }}</v-icon>
        </v-btn>
      </router-link>
    </v-app-bar>

    <v-content>
      <v-container fluid fill-height>
        <v-layout align-center justify-center>
          <v-flex text-center>
            <router-view />
          </v-flex>
        </v-layout>
      </v-container>
    </v-content>
    <Footer />
    <Snackbar />
  </v-app>
</template>

<script lang="ts">
import Vue from "vue";
import { Component } from "vue-property-decorator";
import HelloWorld from "./components/HelloWorld.vue";
import Sider from "./components/Sider.vue";
import Header from "./components/Header.vue";
import Footer from "./components/Footer.vue";
import Snackbar from "./components/Snackbar.vue";
import { BASE_URL } from "@/globals/globals";

class Club {
  url: string = "";
  name: string = "";
  intro: string = "";
  avatar: any;
}

@Component({
  components: {
    Sider,
    Header,
    Footer,
    Snackbar
  }
})
export default class Hello extends Vue {
  name: String = "App";
  club_url = {};
  clubs: Array<Club> = [];
  drawer = true;
  headers = [
    // {
    //   text: "个人",
    //   icon: "account",
    //   link: ""
    // },
    {
      text: "身份",
      icon: "shield-account",
      link: "/membership"
    },
    {
      text: "社团",
      icon: "home-heart",
      link: "/applicant"
    },
    {
      text: "成员",
      icon: "account-group",
      link: "/members"
    }
  ];
  // TODO: 成员是社团已有的所有成员 MEMBER
  // TODO: 社团管理所有已经报名的人 TIMELINE
  // TODO: 批量生成timeline 功能
  // TODO: 确认面试通过的功能
  onChooseClub() {
    if (!this.club_url) return;
    this.$store.commit("initializeInterview", this.club_url);
    this.$router.push("/");
  }

  get owned_clubs() {
    return this.clubs;
  }

  created() {
    // 初始化 owned_club
    this.$http
      .get(`${BASE_URL}/api-admin/user/owned_clubs/`)
      .then((response: any) => {
        console.log(response);
        if (response.status == 200) {
          this.clubs = response.data;
          if (this.clubs.length > 0) {
            this.club_url = this.clubs[0].url;
            this.onChooseClub();
            this.$store.commit("initializeMemberships");
          }
        }
      })
      .finally(() => {});
  }
}
</script>
