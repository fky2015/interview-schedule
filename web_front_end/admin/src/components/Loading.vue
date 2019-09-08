<template>
  <v-progress-linear
    :active="loading.show"
    :indeterminate="loading.show"
    absolute
    top
    color="yellow accent-4"
  ></v-progress-linear>
</template>

<script>
export default {
  computed: {
    loading() {
      return this.$store.state.loading;
    }
  }
};
</script>

<style>
</style>