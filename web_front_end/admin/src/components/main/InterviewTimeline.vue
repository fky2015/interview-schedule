<template>
  <div>
    <div>{{ interviewTimeline }}</div>
    <v-container grid-list-md text-center align-center justify-center>
      <v-data-table
        :headers="headers"
        :items="timelines"
        sort-by="calories"
        class="elevation-1"
      >
        <template v-slot:top>
          <v-toolbar flat color="white">
            <v-toolbar-title>My CRUD</v-toolbar-title>
            <v-divider class="mx-4" inset vertical></v-divider>
            <div class="flex-grow-1"></div>
            <v-dialog v-model="dialog" max-width="500px">
              <template v-slot:activator="{ on }">
                <v-btn color="primary" dark class="mb-2" v-on="on"
                  >New Item</v-btn
                >
              </template>
              <v-card>
                <v-card-title>
                  <span class="headline">{{ formTitle }}</span>
                </v-card-title>

                <v-card-text>
                  <v-container>
                    <!--       {
        text: "开始时间",
        align: "left",
        sortable: false,
        value: "startTime"
      },
      { text: "长度", value: "duration" },
      { text: "用户", value: "user" },
      { text: "是否通过", value: "passed" },
                    { text: "timeID", value: "timeID" },-->

                    <v-row>
                      <v-col cols="12" sm="6" md="4">
                        <v-menu
                          ref="menu"
                          v-model="menu"
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
                              v-model="editedItem.startTime"
                              label="开始时间"
                              readonly
                              v-on="on"
                            ></v-text-field>
                          </template>
                          <v-time-picker
                            v-if="menu"
                            v-model="editedItem.startTime"
                            full-width
                            @click:minute="
                              $refs.menu.save(editedItem.startTime)
                            "
                          ></v-time-picker>
                        </v-menu>
                        <!-- <v-text-field v-model="editedItem.startTime" label="开始时间"></v-text-field> -->
                      </v-col>
                      <v-col cols="12" sm="6" md="4">
                        <v-text-field
                          v-model="editedItem.duration"
                          label="时长"
                        ></v-text-field>
                      </v-col>
                      <v-col cols="12" sm="6" md="4">
                        <v-text-field
                          v-model="editedItem.user"
                          label="用户"
                        ></v-text-field>
                      </v-col>
                      <v-col cols="12" sm="6" md="4">
                        <v-checkbox
                          v-model="editedItem.carbs"
                          label="是否通过"
                        ></v-checkbox>
                      </v-col>
                      <v-col cols="12" sm="6" md="4">
                        <v-text-field
                          v-model="editedItem.timeID"
                          label="同时间区分ID"
                        ></v-text-field>
                      </v-col>
                    </v-row>
                  </v-container>
                </v-card-text>

                <v-card-actions>
                  <div class="flex-grow-1"></div>
                  <v-btn color="blue darken-1" text @click="close"
                    >Cancel</v-btn
                  >
                  <v-btn color="blue darken-1" text @click="save">Save</v-btn>
                </v-card-actions>
              </v-card>
            </v-dialog>
          </v-toolbar>
        </template>
        <template v-slot:item.action="{ item }">
          <v-icon small class="mr-2" @click="editItem(item)">mdi-pencil</v-icon>
          <v-icon small @click="deleteItem(item)">mdi-delete</v-icon>
        </template>
        <template v-slot:no-data>
          <v-btn color="primary" @click="initialize">Reset</v-btn>
        </template>
      </v-data-table>
    </v-container>
    <BatchAdd :url="interviewTimeline.url" :timelines="timelines" />
  </div>
</template>

<script>
import Timeline from "./Timeline.vue";
import BatchAdd from "./BatchAdd.vue";
export default {
  components: {
    BatchAdd
  },
  data: () => ({
    menu: false,
    timelines: [],
    dialog: false,
    dialog_batch: false,
    headers: [
      {
        text: "开始时间",
        align: "left",
        sortable: false,
        value: "startTime"
      },
      { text: "长度", value: "duration" },
      { text: "用户", value: "user" },
      { text: "是否通过", value: "passed" },
      { text: "timeID", value: "timeID" },
      { text: "Actions", value: "action", sortable: false }
    ],
    editedIndex: -1,
    editedItem: {
      startTime: "",
      duration: 10,
      passed: false,
      timeID: 0
    },
    defaultItem: {
      startTime: "",
      duration: 10,
      passed: false,
      timeID: 0
    }
  }),
  computed: {
    index() {
      return this.$route.params.index;
    },
    inner_index() {
      return this.$route.params.inner_index;
    },
    interviewTimeline() {
      return this.$store.state.interview[this.index].interviewTimeline[
        this.inner_index
      ];
    },

    formTitle() {
      return this.editedIndex === -1 ? "New Item" : "Edit Item";
    }
  },
  watch: {
    dialog(val) {
      val || this.close();
    },
    "interviewTimeline.url"() {
      console.log("interviewTimeline changed");
      this.initialize();
    }
  },

  created() {
    this.initialize();
  },

  methods: {
    initialize() {
      this.axios
        .get(`${this.interviewTimeline.url}timeline/`)
        .then(({ data }) => {
          this.timelines = data;
        });
    },

    editItem(item) {
      this.editedIndex = this.timelines.indexOf(item);
      this.editedItem = Object.assign({}, item);
      this.dialog = true;
    },

    deleteItem(item) {
      const index = this.timelines.indexOf(item);
      if (confirm("确认删除该面试场次?")) {
        this.axios
          .delete(item.url)
          .then(({ data }) => {
            this.$store.commit("popSuccess");
          })
          .catch(e => this.$store.commit("popError", e));
        this.timelines.splice(index, 1);
      }
    },

    close() {
      this.dialog = false;
      setTimeout(() => {
        this.editedItem = Object.assign({}, this.defaultItem);
        this.editedIndex = -1;
      }, 300);
    },

    save() {
      // TODO: axios
      if (this.editedIndex > -1) {
        // update
        let ei = this.editedIndex;

        this.axios
          .put(this.timelines[this.editedIndex].url, {
            ...this.editedItem
          })
          .then(({ data }) => {
            this.$store.commit("popSuccess");
            console.log(this.timelines);
            console.log(data);
            Object.assign(this.timelines[ei], data);
          })
          .catch(e => this.$store.commit("popError", e));
      } else {
        // create
        this.axios
          .post("/api-admin/timeline/", {
            user: null,
            interviewTimeline: this.interviewTimeline.url,
            ...this.editedItem
          })
          .then(({ data }) => {
            this.$store.commit("popSuccess");

            this.timelines.push(data);
          })
          .catch(e => this.$store.commit("popError", e));
      }
      this.close();
    }
  }
};
</script>

<style></style>
