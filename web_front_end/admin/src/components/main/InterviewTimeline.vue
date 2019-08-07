<template>
  <div>
    <div>{{ it }}</div>
    <v-container grid-list-md text-center align-center justify-center>
      <v-layout wrap>
        <Timeline
          v-for="(timeline, index) in timelines"
          :key="index"
          :timeline="timeline"
        />
      </v-layout>
    </v-container>
  </div>
</template>

<script>
import Timeline from "./Timeline.vue";
export default {
  components: {
    Timeline
  },
  data: () => ({
    it: {
      url: "http://127.0.0.1:8002/api-admin/interviewTimeline/7/",
      pk: 7,
      interview: "http://127.0.0.1:8002/api-admin/interview/9/",
      location: "教室1"
    },
    timelines: [
      {
        url: "http://127.0.0.1:8002/api-admin/timeline/3/",
        interviewTimeline:
          "http://127.0.0.1:8002/api-admin/interviewTimeline/7/",
        user: null,
        startTime: "2019-08-07T01:00:00Z",
        duration: 10,
        passed: false,
        timeID: 0
      },
      {
        url: "http://127.0.0.1:8002/api-admin/timeline/4/",
        interviewTimeline:
          "http://127.0.0.1:8002/api-admin/interviewTimeline/7/",
        user: null,
        startTime: "2019-08-07T01:00:00Z",
        duration: 10,
        passed: false,
        timeID: 0
      },
      {
        url: "http://127.0.0.1:8002/api-admin/timeline/4/",
        interviewTimeline:
          "http://127.0.0.1:8002/api-admin/interviewTimeline/7/",
        user: null,
        startTime: "2019-08-07T01:00:00Z",
        duration: 10,
        passed: false,
        timeID: 0
      },
      {
        url: "http://127.0.0.1:8002/api-admin/timeline/4/",
        interviewTimeline:
          "http://127.0.0.1:8002/api-admin/interviewTimeline/7/",
        user: null,
        startTime: "2019-08-07T01:00:00Z",
        duration: 10,
        passed: false,
        timeID: 0
      },
      {
        url: "http://127.0.0.1:8002/api-admin/timeline/4/",
        interviewTimeline:
          "http://127.0.0.1:8002/api-admin/interviewTimeline/7/",
        user: null,
        startTime: "2019-08-07T01:00:00Z",
        duration: 10,
        passed: false,
        timeID: 0
      },
      {
        url: "http://127.0.0.1:8002/api-admin/timeline/4/",
        interviewTimeline:
          "http://127.0.0.1:8002/api-admin/interviewTimeline/7/",
        user: null,
        startTime: "2019-08-07T01:00:00Z",
        duration: 10,
        passed: false,
        timeID: 0
      },
      {
        url: "http://127.0.0.1:8002/api-admin/timeline/4/",
        interviewTimeline:
          "http://127.0.0.1:8002/api-admin/interviewTimeline/7/",
        user: null,
        startTime: "2019-08-07T01:00:00Z",
        duration: 10,
        passed: false,
        timeID: 0
      },
      {
        url: "http://127.0.0.1:8002/api-admin/timeline/4/",
        interviewTimeline:
          "http://127.0.0.1:8002/api-admin/interviewTimeline/7/",
        user: null,
        startTime: "2019-08-07T01:00:00Z",
        duration: 10,
        passed: false,
        timeID: 0
      },
      {
        url: "http://127.0.0.1:8002/api-admin/timeline/4/",
        interviewTimeline:
          "http://127.0.0.1:8002/api-admin/interviewTimeline/7/",
        user: null,
        startTime: "2019-08-07T01:00:00Z",
        duration: 10,
        passed: false,
        timeID: 0
      },
      {
        url: "http://127.0.0.1:8002/api-admin/timeline/4/",
        interviewTimeline:
          "http://127.0.0.1:8002/api-admin/interviewTimeline/7/",
        user: null,
        startTime: "2019-08-07T01:00:00Z",
        duration: 10,
        passed: false,
        timeID: 0
      },
      {
        url: "http://127.0.0.1:8002/api-admin/timeline/4/",
        interviewTimeline:
          "http://127.0.0.1:8002/api-admin/interviewTimeline/7/",
        user: null,
        startTime: "2019-08-07T01:00:00Z",
        duration: 10,
        passed: false,
        timeID: 0
      },
      {
        url: "http://127.0.0.1:8002/api-admin/timeline/4/",
        interviewTimeline:
          "http://127.0.0.1:8002/api-admin/interviewTimeline/7/",
        user: null,
        startTime: "2019-08-07T01:00:00Z",
        duration: 10,
        passed: false,
        timeID: 0
      },
      {
        url: "http://127.0.0.1:8002/api-admin/timeline/4/",
        interviewTimeline:
          "http://127.0.0.1:8002/api-admin/interviewTimeline/7/",
        user: null,
        startTime: "2019-08-07T01:00:00Z",
        duration: 10,
        passed: false,
        timeID: 0
      },
      {
        url: "http://127.0.0.1:8002/api-admin/timeline/4/",
        interviewTimeline:
          "http://127.0.0.1:8002/api-admin/interviewTimeline/7/",
        user: null,
        startTime: "2019-08-07T01:00:00Z",
        duration: 10,
        passed: false,
        timeID: 0
      }
    ]
  })
};
</script>

<style></style>
