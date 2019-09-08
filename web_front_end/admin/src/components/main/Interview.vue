<template>
  <div>
    interview : {{ interview }}
    <InterviewData :interview="interview" />
    <v-data-table
      :headers="headers"
      :items="interview.interviewTimeline"
      sort-by="calories"
      class="elevation-1"
    >
      <template v-slot:top>
        <v-toolbar flat color="white">
          <v-toolbar-title>教室管理</v-toolbar-title>
          <v-divider class="mx-4" inset vertical></v-divider>
          <v-spacer></v-spacer>
          <v-dialog v-model="dialog" max-width="500px">
            <template v-slot:activator="{ on }">
              <v-btn color="primary" dark class="mb-2" v-on="on"
                >新建教室</v-btn
              >
            </template>
            <v-card>
              <v-card-title>
                <span class="headline">{{ formTitle }}</span>
              </v-card-title>

              <v-card-text>
                <v-container grid-list-md>
                  <v-layout wrap>
                    <v-flex xs12 sm6 md4>
                      <v-text-field
                        v-model="editedItem.location"
                        label="地点"
                      ></v-text-field>
                    </v-flex>
                    <v-flex xs12 sm6 md4>
                      <v-menu
                        v-model="menu"
                        :close-on-content-click="false"
                        :nudge-right="40"
                        transition="scale-transition"
                        offset-y
                        full-width
                        min-width="290px"
                      >
                        <template v-slot:activator="{ on }">
                          <v-text-field
                            v-model="editedItem.date"
                            label="Picker without buttons"
                            readonly
                            v-on="on"
                          ></v-text-field>
                        </template>
                        <v-date-picker
                          v-model="editedItem.date"
                          @input="menu = false"
                        ></v-date-picker>
                      </v-menu>
                    </v-flex>
                    <v-flex xs12 sm6 md4>
                      <v-text-field
                        v-model="editedItem.remarks"
                        label="描述"
                      ></v-text-field>
                    </v-flex>
                  </v-layout>
                </v-container>
              </v-card-text>

              <v-card-actions>
                <v-spacer></v-spacer>
                <v-btn color="blue darken-1" text @click="close">取消</v-btn>
                <v-btn color="blue darken-1" text @click="save">保存</v-btn>
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
        <v-btn color="primary" @click>Reset</v-btn>
      </template>
    </v-data-table>
  </div>
</template>

<script>
import InterviewData from "./InterviewData.vue";
import { BASE_URL } from "@/globals/globals";

export default {
  components: {
    InterviewData
  },
  data: () => ({
    menu: false,
    editedItem: {
      localtion: "",
      date: "",
      remarks: ""
    },
    editedIndex: -1,
    defaultItem: {
      localtion: "",
      date: "",
      remarks: ""
    },
    dialog: false,
    headers: [
      {
        text: "location",
        value: "location"
      },
      {
        text: "date",
        value: "date"
      },
      {
        text: "remarks",
        value: "remarks"
      },
      { text: "Actions", value: "action", sortable: false }
    ]
  }),
  mounted() {},
  computed: {
    formTitle() {
      return this.editedIndex === -1 ? "新建教室" : "编辑教室";
    },
    index() {
      return this.$route.params.index;
    },
    interview() {
      return this.$store.state.interview[this.index];
    }
  },
  watch: {
    dialog(val) {
      val || this.close();
    }
  },

  created() {
    this.initialize();
  },
  methods: {
    initialize() {
      this.$store.commit("initializeMemberships");
    },
    editItem(item) {
      this.editedIndex = this.interview.interviewTimeline.indexOf(item);
      this.editedItem = Object.assign({}, item);
      this.dialog = true;
    },

    deleteItem(item) {
      const index = this.interview.interviewTimeline.indexOf(item);
      if (confirm("确定删除这个教室场次信息?")) {
        this.axios
          .delete(item.url)
          .then(({ data }) => {
            this.$store.commit("popSuccess");
          })
          .catch(e => this.$store.commit("popError", e));
        this.interview.interviewTimeline.splice(index, 1);
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
      if (this.editedIndex > -1) {
        // update
        this.axios
          .put(
            this.interview.interviewTimeline[this.editedIndex].url,
            this.editedItem
          )
          .then(({ data }) => {
            this.$store.commit("popSuccess");
            Object.assign(
              this.interview.interviewTimeline[this.editedIndex],
              data
            );
            this.close();
          })
          .catch(e => this.$store.commit("popError", e));
      } else {
        // create
        this.axios
          .post(`${BASE_URL}/api-admin/interviewTimeline/`, {
            interview: this.interview.url,
            ...this.editedItem
          })
          .then(({ data }) => {
            this.interview.interviewTimeline.push(data);
            this.$store.commit("popSuccess");
            this.close();
          })
          .catch(e => this.$store.commit("popError", e));
      }
    }
  }
};
</script>

<style></style>
