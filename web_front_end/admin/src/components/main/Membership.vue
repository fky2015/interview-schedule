<template>
  <div>
    <v-data-table
      :headers="headers"
      :items="filtered_memberships"
      sort-by="calories"
      class="elevation-1"
    >
      <template v-slot:top>
        <v-toolbar flat color="white">
          <v-toolbar-title>My CRUD</v-toolbar-title>
          <v-divider class="mx-4" inset vertical></v-divider>
          <v-spacer></v-spacer>
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
                  <v-row>
                    <v-col cols="12" sm="6" md="6">
                      <v-text-field
                        v-model="editedItem.name"
                        label="名称"
                      ></v-text-field>
                    </v-col>
                    <v-col cols="12" sm="6" md="6">
                      <v-checkbox
                        v-model="editedItem.is_admin"
                        label="是否为管理员"
                      ></v-checkbox>
                    </v-col>
                  </v-row>
                </v-container>
              </v-card-text>

              <v-card-actions>
                <v-spacer></v-spacer>
                <v-btn color="blue darken-1" text @click="close">Cancel</v-btn>
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
    <div>memberships: {{ memberships }}</div>
    <div>filtered_memberships: {{ filtered_memberships }}</div>
  </div>
</template>

<script>
import { BASE_URL } from "@/globals/globals";

export default {
  data: () => ({
    dialog: false,
    headers: [
      {
        text: "名称",
        align: "left",
        sortable: false,
        value: "name"
      },
      {
        text: "是否为admin",
        value: "is_admin"
      },
      {
        text: "创建时间",
        value: "date_created"
      },
      { text: "Actions", value: "action", sortable: false }
    ],
    editedIndex: -1,
    editedItem: {
      name: "",
      is_admin: false
    },
    defaultItem: {
      name: "",
      is_admin: false
    }
  }),

  computed: {
    formTitle() {
      return this.editedIndex === -1 ? "New Item" : "Edit Item";
    },
    memberships() {
      return this.$store.state.memberships;
    },
    filtered_memberships() {
      return this.memberships.map(v => ({
        ...v,
        is_admin: v.is_admin ? "是" : "否"
      }));
    },
    club_url() {
      return this.$store.state.club_url;
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
      this.editedIndex = this.filtered_memberships.indexOf(item);
      this.editedItem = Object.assign({}, this.memberships[this.editedIndex]);

      this.dialog = true;
    },

    deleteItem(item) {
      const index = this.filtered_memberships.indexOf(item);
      if (confirm("确定删除这个成员身份?")) {
        this.axios.delete(item.url).then(() => {
          this.memberships.splice(index, 1);
          this.filtered_memberships.splice(index, 1);
        });
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
        let editedIndex = this.editedIndex;
        // update
        this.axios
          .put(this.memberships[editedIndex].url, {
            ...this.editedItem
          })
          .then(({ data, status }) => {
            // this.editedItem well become -1, but I don't know why.
            if (status == 200) {
              Object.assign(this.memberships[editedIndex], data);
            } else if (status >= 400) {
              this.$store.commit("popError", data);
            }
          })
          .catch(error => {
            this.$store.commit("popError", error);
          });
      } else {
        // create
        this.axios
          .post(`${BASE_URL}/api-admin/membership/`, {
            club: this.club_url,
            ...this.editedItem
          })
          .then(({ data, status }) => {
            if (status == 201) {
              this.memberships.push(data);
              this.$store.commit("popSuccess");
            }
          });
      }
      this.close();
    }
  }
};
</script>

<style></style>
