<template>
  <v-dialog v-model="dialog" persistent max-width="600px">
    <template v-slot:activator="{ on }">
      <v-btn color="primary" dark v-on="on">批量添加</v-btn>
    </template>
    <v-card>
      <v-card-title>
        <span class="headline">批量添加面试时间</span>
      </v-card-title>
      <v-card-text>
        <v-form ref="form" v-model="valid" :lazy-validation="lazy">
          <v-menu
            ref="menu"
            v-model="menu1"
            :close-on-content-click="false"
            :nudge-right="40"
            :return-value.sync="time"
            transition="scale-transition"
            offset-y
            full-width
            max-width="290px"
            min-width="290px"
          >
            <template v-slot:activator="{ on }">
              <v-text-field
                v-model="startTime"
                :rules="startTimeRules"
                label="startTime"
                required
                v-on="on"
                readonly
              ></v-text-field>
            </template>
            <v-time-picker
              v-if="menu1"
              v-model="startTime"
              full-width
              @click:minute="$refs.menu.save(startTime)"
            ></v-time-picker>
          </v-menu>

          <v-menu
            ref="menu"
            v-model="menu2"
            :close-on-content-click="false"
            :nudge-right="40"
            :return-value.sync="time"
            transition="scale-transition"
            offset-y
            full-width
            max-width="290px"
            min-width="290px"
          >
            <template v-slot:activator="{ on }">
              <v-text-field
                v-model="endTime"
                v-on="on"
                label="endTime"
                readonly
                required
              ></v-text-field>
            </template>
            <v-time-picker
              v-if="menu2"
              v-model="endTime"
              full-width
              @click:minute="$refs.menu.save(endTime)"
            ></v-time-picker>
          </v-menu>

          <v-text-field
            v-model="duration"
            :rules="durationRules"
            label="duration"
            required
          ></v-text-field>
        </v-form>
        <div>一共可面试 - {{ repeat }} - 人</div>
      </v-card-text>
      <v-card-actions>
        <v-spacer></v-spacer>
        <v-btn color="error" class="mr-4" @click="dialog = false">取消</v-btn>

        <v-btn color="success" @click="submit">确认</v-btn>
      </v-card-actions>
    </v-card>
  </v-dialog>
</template>

<script>
export default {
  data: () => ({
    valid: true,
    dialog: false,
    menu1: false,
    menu2: false,
    startTime: "",
    endTime: "",
    replica: 1,
    replicaRules: [
      v => !!v || "replica is required",
      v => (v && v >= 0) || "must be an positive integer."
    ],
    startTimeRules: [
      v => !!v || "startTime is required",
      v => (v && v.length <= 10) || "startTime must be less than 10 characters"
    ],
    duration: 10,
    durationRules: [v => !!v || "E-mail is required"]
    // select: null,
    // items: ["Item 1", "Item 2", "Item 3", "Item 4"],
  }),
  computed: {
    repeat() {
      return this.getDuration(this.startTime, this.endTime) / this.duration;
    }
  },
  props: ["url", "timelines"],
  methods: {
    getDuration(start, end) {
      let start_hour = parseInt(start.slice(0, 2));
      let start_mins = parseInt(start.slice(3, 5));
      let end_hour = parseInt(end.slice(0, 2));
      let end_mins = parseInt(end.slice(3, 5));
      return (end_hour - start_hour) * 60 + end_mins - start_mins;
    },
    validate() {
      if (this.$refs.form.validate()) {
        this.snackbar = true;
        return true;
      }
      return false;
    },
    reset() {
      this.$refs.form.reset();
    },
    resetValidation() {
      this.$refs.form.resetValidation();
    },
    submit() {
      if (this.validate()) {
        if (this.repeat < 1) {
          this.$store.commit("popError", "请修改 开始/结束 时间");
          return;
        }
        let list = [];
        let startTime = new Date();
        startTime.setHours(this.startTime.slice(0, 2));
        startTime.setMinutes(this.startTime.slice(3, 5));
        startTime.setSeconds(0);

        for (let i = 0; i < this.repeat; i++) {
          let _temp = startTime.toTimeString();
          _temp = _temp.slice(0, 8);

          list.push({
            interviewTimeline: this.url,
            user: null,
            startTime: _temp,
            duration: this.duration,
            timeID: 0
          });

          startTime = new Date(startTime.getTime() + this.duration * 60000);
        }

        this.axios
          .post("/api-admin/timeline/", list)
          .then(({ data }) => {
            console.log(data);
            this.$store.commit("popSuccess");
            this.timelines = this.timeline.concat(data);
          })
          .catch(e => this.$store.commit("popError", e));
        console.log(list);
      }
    }
  }
};
</script>

<style></style>
