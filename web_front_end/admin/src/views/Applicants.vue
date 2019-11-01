<template>
  <v-card>
    <v-card-title>
      报名信息
      <v-spacer></v-spacer>
      <v-text-field
        v-model="search"
        append-icon="mdi-search"
        label="Search"
        single-line
        hide-details
      ></v-text-field>
    </v-card-title>
    <v-data-table
      :loading="loading"
      :headers="headers"
      :items="applicants"
      :search="search"
    >
      <template v-slot:item.user="{ item }">{{ item.user.realname }}</template>
      <template v-slot:item.date="{ item }">
        {{ item.interviewTimeline.date }}
      </template>
      <template v-slot:item.location="{ item }">
        {{ item.interviewTimeline.location }}
      </template>
    </v-data-table>
    <v-card-actions>
      <v-btn block @click="exportData">导出</v-btn>
    </v-card-actions>
  </v-card>
</template>

<script>
import { exportCSV } from "@/utils/utils";
export default {
  data: () => ({
    search: "",
    headers: [
      {
        text: "姓名",
        align: "left",
        sortable: false,
        value: "user"
      },
      { text: "地点", value: "location" },
      { text: "日期", value: "date" },
      { text: "时间", value: "startTime" },
      { text: "持续时间(mins)", value: "duration" }
    ],
    applicants: [],
    loading: false
  }),
  computed: {
    club_url() {
      return this.$store.state.club_url;
    }
  },
  methods: {
    getApplicants() {
      this.loading = true;
      this.axios
        .get(`${this.club_url}applicants/`)
        .then(({ data }) => {
          this.applicants = data;
        })
        .catch(() => {})
        .finally(() => {
          this.loading = false;
        });
    },
    customFilter(value, search, item) {
      // TODO
      return (
        value != null &&
        search != null &&
        typeof (value === "string") &&
        JSON.stringify(value).indexOf(search) !== -1
      );
    },
    exportData() {
      // export to csv
      let rows = this.applicants.map(v => [
        v.user.username,
        v.user.realname,
        v.user.studentNumber,
        v.user.email,
        v.user.mobile,
        v.location,
        v.date,
        v.startTime,
        v.duration,
        v.comment
      ]);
      headers = [
        "用户名",
        "姓名",
        "学号",
        "邮箱",
        "手机号",
        "面试地点",
        "面试日期",
        "开始时间",
        "持续时间",
        "自我评价"
      ];
      exportCSV(rows, headers);
    }
  },
  watch: {
    club_url() {
      this.getApplicants();
    }
  },
  mounted() {},
  created() {
    if (this.club_url === null || this.club_url === "") {
      return;
    }
    this.getApplicants();
  }
};
</script>

<style></style>
