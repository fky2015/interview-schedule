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
  </v-card>
</template>

<script>
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
