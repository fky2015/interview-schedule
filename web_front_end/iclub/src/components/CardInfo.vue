<template>
  <v-container>
    <v-hover>
      <v-card slot-scope="{ hover }" :class="`elevation-${hover ? 8 : 2}`">
        <v-img loading :src="imgUrl" alt="social-pictures"></v-img>

        <v-card-title>
          <v-layout column justify-center align-start>
            <v-flex>
              <v-layout row align-end>
                <v-flex class shrink>
                  <v-avatar size="64">
                    <v-img
                      src="http://img.touxiangzhan.com/upload/image/4a1490838412n2103307902t15.jpg"
                    ></v-img>
                  </v-avatar>
                </v-flex>
                <v-flex>
                  <h1 class="font-weight-thin" shrink>
                    学生电视中心
                    <hr class>
                  </h1>
                </v-flex>
              </v-layout>
            </v-flex>
            <v-flex>
              <br>
            </v-flex>
            <v-flex>
              <span>
                学生电视中心是北京理工大学团委下辖的学生影视组织。学生电视中心是北京理工大学团委下辖的学生影视组织。
                学生电视中心是北京理工大学团委下辖的学生影视组织。学生电视中心是北京理工大学团委下辖的学生影视组织。
              </span>
            </v-flex>
          </v-layout>
        </v-card-title>

        <v-card-actions>
          <v-spacer/>
          <v-btn depressed href="#/sign-up" class="red lighten-1 white--text">更多</v-btn>
          <v-btn depressed href="#/sign-up" class="red lighten-1 white--text">加入</v-btn>
          <v-spacer/>
        </v-card-actions>
        <br>
      </v-card>
    </v-hover>
  </v-container>
</template>
<script>
export default {
  props: {
    clubId: {
      default: "001"
    },
    imgUrl: {
      default: "http://upload.art.ifeng.com/2017/0425/1493105660290.jpg"
    }
  }
};
</script>
<style>
</style>
