<template>
  <v-snackbar v-model="snackbar.show">
    {{ snackbar.text }}
    <v-btn color="pink" text @click="snackbar.show = false">Close</v-btn>
  </v-snackbar>
</template>

<script>
export default {
  computed: {
    snackbar() {
      return this.$store.state.snackbar;
    }
  }
};
</script>

<style>
</style>