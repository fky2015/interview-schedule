<template>
  <v-flex xs6 md4 lg3>
    <v-hover v-slot:default="{ hover }">
      <v-card :elevation="hover ? 12 : 2" class="mx-auto">
        <v-card-text class="my-4 text-center title">
          {{ time }}
          {{ timeline.duration }}</v-card-text
        >
      </v-card>
    </v-hover>
  </v-flex>
</template>

<script>
export default {
  props: {
    timeline: {
      type: Object,
      required: true,
      default: () => ({
        url: "http://127.0.0.1:8002/api-admin/timeline/3/",
        interviewTimeline:
          "http://127.0.0.1:8002/api-admin/interviewTimeline/7/",
        user: null,
        startTime: "2019-08-07T01:00:00Z",
        duration: 10,
        passed: false,
        timeID: 0
      })
    }
  },
  data: () => ({}),
  computed: {
    time() {
      return new Date(this.timeline.startTime).toLocaleTimeString();
    }
  }
};
</script>

<style></style>
