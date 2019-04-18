<template>
  <v-container class="container elevation-3">
    <v-layout align-center column>
      <h1 class="display-3" id="title">
        社团广场
        <hr class="title-underline">
      </h1>
      <hr class="title-underline">
    </v-layout>
    <card-info v-for="i in 10" :key="i"></card-info>
  </v-container>
</template>
<script>
import CardInfo from "../components/CardInfo";
export default {
  components: {
    CardInfo
  }
};
</script>
<style>
#title {
  padding: 10px;
}
.title-underline {
  border: 1px solid;
}
</style>
