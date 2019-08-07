<template>
  <v-list>
    <router-link :to="'/interview/' + data.pk">
      <v-list-item @click="">
        <v-list-item-title>{{ data.title }}</v-list-item-title>
      </v-list-item>
    </router-link>
    <v-list-item @click="">
      <v-list-item-content
        v-for="(room, index) in data.InterviewTimeline"
        :key="index"
      >
        <router-link :to="'/interview-timeline/' + room.pk">
          <v-list-item-subtitle>{{ room.location }}</v-list-item-subtitle>
        </router-link>
      </v-list-item-content>
    </v-list-item>
  </v-list>
</template>

<script>
export default {
  props: {
    data: {
      type: Object,
      required: true,
      default: () => ({
        url: "http://127.0.0.1:8002/api-admin/interview/9/",
        title: "test2",
        edit_finish: false,
        is_public: false,
        InterviewTimeline: [
          {
            url: "http://127.0.0.1:8002/api-admin/interviewTimeline/7/",
            interview: "http://127.0.0.1:8002/api-admin/interview/9/",
            location: "教室1"
          }
        ]
      })
    }
  }
};
</script>

<style></style>
