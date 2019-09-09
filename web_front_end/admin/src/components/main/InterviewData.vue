<template>
  <v-card class="elevation-1">
    <v-card-title>
      <v-row>
        <v-col class="text-left" cols="6">{{ interview.title }}</v-col>
        <v-col class="font-weight-light" cols="3">{{
          interview.edit_finish ? "完成修改" : "未完成修改"
        }}</v-col>
        <v-col class="font-weight-light" cols="3">
          {{ interview.is_public ? "对外开放" : "未对外开放" }}
        </v-col>
      </v-row>
    </v-card-title>
    <v-card-text>
      {{ interview.description }}
    </v-card-text>
    <v-card-actions>
      <v-dialog v-model="dialog" width="500">
        <template v-slot:activator="{ on }">
          <v-btn color="red lighten-2" dark v-on="on">编辑信息</v-btn>
        </template>

        <v-card>
          <v-card-title class="headline grey lighten-2" primary-title
            >修改本次面试信息</v-card-title
          >

          <v-card-text>
            <InterviewForm :interview="interview" />
          </v-card-text>

          <v-divider></v-divider>

          <v-card-actions>
            <v-spacer></v-spacer>
            <v-btn color="error" text @click="deleteInterview">删除</v-btn>
            <v-btn color="primary" text @click="saveInterview">修改</v-btn>
          </v-card-actions>
        </v-card>
      </v-dialog>
    </v-card-actions>
    <v-divider></v-divider>
    <v-card flat>
      <v-card-text>
        <v-row>
          <v-col cols="11">
            <v-select
              label="准入状态"
              v-model="inStateOnlyUrl"
              :items="memberships"
              item-text="name"
              item-value="url"
              multiple
            ></v-select
          ></v-col>
          <v-col cols="1"><v-btn @click="saveInState">save</v-btn></v-col>
        </v-row>
        <v-row>
          <v-col cols="11">
            <v-select
              label="跳转状态"
              v-model="interview.out_state"
              :items="memberships"
              item-text="name"
              item-value="url"
            ></v-select
          ></v-col>
          <v-col cols="1"><v-btn @click="saveInterview">save</v-btn></v-col>
        </v-row>
      </v-card-text>
    </v-card>
  </v-card>
</template>

<script>
import InterviewForm from "@/components/forms/InterviewForm";
import { BASE_URL } from "@/globals/globals.ts";
export default {
  components: { InterviewForm },
  props: ["interview"],
  data: () => ({
    dialog: false,
    inState: [],
    inStateOnlyUrl: [],
    outState: {}
  }),
  watch: {
    "interview.out_state"() {
      console.log("out_state_change");
      // this.initializeOutState();
    },
    "interview.url"() {
      console.log("interview changed");
      this.initializeInState();
    }
  },
  computed: {
    memberships() {
      return this.$store.state.memberships;
    }
  },
  methods: {
    deleteInterview() {
      this.$http.delete(this.$props.interview.url).then(({ status }) => {
        if (status < 300 && status >= 200) {
          this.$store.commit("popSuccess");
          this.$router.push("home");
        }
      });
    },
    saveInterview() {
      this.$http
        .put(this.interview.url, {
          ...this.interview
        })
        .then(({ data, status }) => {
          if (status == 200) {
            this.$store.commit("popSuccess");
          }
        });
    },
    initializeInState() {
      if (!this.interview.url) {
        this.$router.push("home");
      }
      this.axios
        .get(`${this.interview.url}instate/`)
        .then(({ data, status }) => {
          this.inState = data;
          this.inStateOnlyUrl = data.map(v => v.membership);
        })
        .catch(e => this.$store.commit("popError", e));
    },
    initializeOutState() {
      this.axios.get(`${this.interview.out_state}`).then(({ data }) => {
        this.outState = data;
      });
    },
    saveInState() {
      // create new state
      let temp_inState = this.inState.map(v => v.membership);
      let new_inState = this.inStateOnlyUrl
        .filter(v => !temp_inState.includes(v))
        .map(v => ({
          interview: this.interview.url,
          membership: v
        }));
      for (let obj of new_inState) {
        this.axios
          .post(`${BASE_URL}/api-admin/instate/`, obj)
          .then(({ data }) => {
            this.$store.commit("popSuccess");
          })
          .catch(e => this.$store.commit("popError", e));
      }

      // delete old state
      let old_inState = this.inState.filter(
        v => !this.inStateOnlyUrl.includes(v.membership)
      );
      console.log(old_inState);

      for (let obj of old_inState) {
        this.axios
          .delete(obj.url)
          .then(() => {})
          .catch(e => this.$store.commit("popError", e));
      }
    },
    saveOutState() {}
  },
  mounted() {
    // initialize Instate
    this.initializeInState();
    // this.initializeOutState();
  }
};
</script>

<style></style>
