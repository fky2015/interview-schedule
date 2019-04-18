<template>
  <v-toolbar>
    <v-toolbar-title class="headline">
      <span class="font-weight-bold">社团面试系统</span>
    </v-toolbar-title>

    <v-btn outline href="#/" class="red--text text--lighten--1">
      <span>广场</span>
    </v-btn>

    <v-spacer></v-spacer>
    <v-btn depressed href="#/me" class="red lighten-1 white--text">
      <span>我的</span>
    </v-btn>
    <v-btn depressed href="#/sign-up" class="red lighten-1 white--text">
      <span>注册</span>
    </v-btn>

    <v-btn
      outline
      href="https://github.com/vuetifyjs/vuetify/releases/latest"
      class="red--text text--lighten--1"
    >
      <span>登陆</span>
    </v-btn>
  </v-toolbar>
</template>
<script>
export default {
  methods: {
    back_to_home: function() {
      this.$router.push("/");
    }
  }
};
</script>
<style>
</style>

