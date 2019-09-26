<template>
  <div>
    <router-link
      :to="{
        name: 'interview',
        params: { index }
      }"
      tag="span"
      :key="index"
    >
      <v-list-item @click="doNothing">
        <v-list-item-title>{{ data.title }}</v-list-item-title>
      </v-list-item>
    </router-link>

    <template
      v-if="
        Array.isArray(data.interviewTimeline) &&
          data.interviewTimeline.length > 0
      "
    >
      <template v-for="(room, inner_index) in data.interviewTimeline">
        <router-link
          :to="{
            name: 'interview-timeline',
            params: { index, inner_index }
          }"
          :key="index + '' + inner_index"
          tag="div"
        >
          <v-list-item @click="doNothing">
            <v-list-item-content>
              <v-list-item-subtitle
                >&nbsp;&nbsp;&nbsp; {{ room.location }}</v-list-item-subtitle
              >
            </v-list-item-content>
          </v-list-item></router-link
        >
      </template>
    </template>
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
