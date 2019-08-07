<template>
  <v-app id="inspire">
    <Sider />

    <Header />

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
  </v-app>
</template>

<script lang="ts">
import Vue from "vue";
import HelloWorld from "./components/HelloWorld.vue";
import Sider from "./components/Sider.vue";
import Header from "./components/Header.vue";
import Footer from "./components/Footer.vue";
export default Vue.extend({
  name: "App",
  components: {
    Sider,
    Header,
    Footer
  },
  data: () => ({
    drawer: null
  })
});
</script>
