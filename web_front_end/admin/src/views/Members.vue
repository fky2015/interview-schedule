<template>
  <v-data-table :headers="headers" :items="members" class="elevation-1">
    <!-- <template v-slot:item.calories="{ item }">
      <v-chip :color="getColor(item.calories)" dark>{{ item.calories }}</v-chip>
    </template> -->
  </v-data-table>
</template>

<script>
export default {
  data() {
    return {
      members: [],
      headers: [
        {
          text: "用户名",
          align: "left",
          sortable: false,
          value: "username"
        },
        { text: "姓名", value: "realname" },
        { text: "邮箱", value: "email" },
        { text: "手机", value: "mobile" }
      ]
    };
  },
  computed: {
    club_url() {
      return this.$store.state.club_url;
    }
  },
  watch: {
    club_url() {
      this.initialize();
    }
  },
  methods: {
    // getColor(calories) {
    //   if (calories > 400) return "red";
    //   else if (calories > 200) return "orange";
    //   else return "green";
    // },
    initialize() {
      if (!this.club_url) return;
      this.axios.get(`${this.club_url}members/`).then(({ data }) => {
        this.members = data;
        this.$store.commit("popSuccess");
      });
    }
  },
  created() {
    this.initialize();
  }
};
</script>

<style></style>
