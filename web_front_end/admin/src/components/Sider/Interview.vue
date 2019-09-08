<template>
  <div>
    <router-link
      :to="{
        name: 'interview',
        params: { index }
      }"
      tag="span"
    >
      <v-list-item @click="doNothing">
        <v-list-item-title>{{ data.title }}</v-list-item-title>
      </v-list-item>
    </router-link>

    <v-list-item
      @click="doNothing"
      v-if="
        Array.isArray(data.interviewTimeline) &&
          data.interviewTimeline.length > 0
      "
    >
      <v-list-item-content
        v-for="(room, inner_index) in data.interviewTimeline"
        :key="inner_index"
      >
        <router-link
          :to="{
            name: 'interview-timeline',
            params: { index, inner_index }
          }"
          tag="div"
        >
          <v-list-item-subtitle
            >&nbsp;&nbsp;&nbsp; {{ room.location }}</v-list-item-subtitle
          >
        </router-link>
      </v-list-item-content>
    </v-list-item>
    {{ data }}
  </div>
</template>

<script lang="ts">
import Vue from "vue";
import { Component, Prop } from "vue-property-decorator";

@Component
export default class Interview extends Vue {
  @Prop(Object) data: object | undefined;
  @Prop(Number) index: number | undefined;
  doNothing() {}
}
</script>

<style></style>
