<template>
  <div>
    <v-list>
      <Interview
        v-for="(d, index) in interview"
        :key="index"
        :data="d"
        :index="index"
      />
    </v-list>
    <v-dialog v-model="new_interview_display" width="500">
      <template v-slot:activator="{ on }">
        <v-btn text block color="red lighten-2" dark v-on="on">新建面试</v-btn>
      </template>
      <v-card>
        <v-card-title class="headline grey lighten-2" primary-title
          >新建面试</v-card-title
        >

        <v-card-text>
          <InterviewForm :interview="new_interview" />
        </v-card-text>

        <v-divider></v-divider>

        <v-card-actions>
          <v-spacer></v-spacer>
          <v-btn color="primary" text @click="newInterview">提交</v-btn>
        </v-card-actions>
      </v-card>
    </v-dialog>
  </div>
</template>

<script lang="ts">
import Vue from "vue";
import { Component, Prop } from "vue-property-decorator";
import Interview from "./Sider/Interview.vue";
import { State } from "vuex-class";
import InterviewForm from "@/components/forms/InterviewForm.vue";
import { BASE_URL } from "@/globals/globals";

@Component({
  components: {
    Interview,
    InterviewForm
  }
})
export default class Sider extends Vue {
  @State interview: any;
  club: string = "";
  drawer: boolean = true;
  new_interview_display: boolean = false;
  new_interview: Object = {
    title: "",
    description: "",
    edit_finish: false,
    is_public: false,
    out_state: ""
  };

  get club_url() {
    return this.$store.state.club_url;
  }

  newInterview() {
    this.axios
      .post(`${BASE_URL}/api-admin/interview/`, {
        club: this.club_url,
        ...this.new_interview
      })
      .then(({ data, status }) => {
        if (status == 201) {
          this.interview.push(data);
          this.$store.commit("popSuccess");
        } else {
          this.$store.commit("popError", data);
        }
      })
      .catch(e => {
        if (e.response && e.response.data)
          this.$store.commit("popError", e.response.data);
      });
    this.new_interview_display = false;
  }

  fetch() {}

  mounted() {
    // use axios to get clubs, and update `data.clubs`,
    // when ever update at clubs' select, update the interview accordingly.
  }
}
</script>

<style></style>
