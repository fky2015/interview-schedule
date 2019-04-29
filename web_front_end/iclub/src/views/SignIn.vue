<template>
  <v-app id="inspire">
    <v-content>
      <v-container fluid fill-height>
        <v-layout align-center justify-center>
          <v-flex xs12 sm8 md4>
            <v-card class="elevation-12">
              <v-toolbar dark color="red lighten--1">
                <v-toolbar-title>登陆</v-toolbar-title>
                <v-spacer></v-spacer>
              </v-toolbar>
              <v-card-text>
                <v-form ref="form" v-model="valid" lazy-validation>
                  <v-text-field
                    color="red"
                    prepend-icon="email"
                    v-model="email"
                    :rules="emailRules"
                    label="电子邮箱"
                    required
                  ></v-text-field>

                  <v-text-field
                    color="red"
                    v-model="password"
                    :rules="passwordRules"
                    label="密码"
                    required
                    prepend-icon="lock"
                    :append-icon="
                      showPassword ? 'visibility' : 'visibility_off'
                    "
                    :type="showPassword ? 'text' : 'password'"
                    @click:append="showPassword = !showPassword"
                    @input="confirm_password = ''"
                  ></v-text-field>
                  <v-btn flat class="red lighten--1 white--text">登陆</v-btn>
                </v-form>
              </v-card-text>
              <v-card-actions></v-card-actions>
            </v-card>
          </v-flex>
        </v-layout>
      </v-container>
    </v-content>
  </v-app>
</template>

<script>
import { constants } from "crypto";
var temp;
export default {
  data: () => ({
    that: this,
    valid: true,
    name: "",
    nameRules: [v => !!v || "请填写昵称"],
    email: "",
    emailRules: [
      v => !!v || "请填写电子邮箱",
      function(v){
          return true||"用户不存在";
      }
    ],
    passwordRules: [
      v => !!v || " 请填写密码",
      function(v) {
        temp = v;
        return true;
      },
      v => (v && v.length >= 6) || "密码长度至少为6位"
    ],
    showPassword: false
  }),
  props: {
    source: String
  },
  computed: {},
  methods: {
    resetConfirmPassword() {
      console.log(confirm_password);
      confirm_password = "";
      console.log(confirm_password);
    },
    validate() {
      if (this.$refs.form.validate()) {
        this.snackbar = true;
      }
    },
    reset() {
      this.$refs.form.reset();
    }
  }
};
</script>
