<template>
  <v-app>
    <tool-bar></tool-bar>
    <router-view />
  </v-app>
</template>
<script>
import HelloWorld from "./components/HelloWorld";
import ToolBar from "./components/ToolBar";
export default {
  
  name: "App",
  components: {
    HelloWorld,
    ToolBar
  },
  data() {
    return {};
  }
};
</script>
