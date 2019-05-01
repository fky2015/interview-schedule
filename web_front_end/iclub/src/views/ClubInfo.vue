<template>
  <v-container class="grey">
    <v-layout column>
      <v-flex>
        <v-hover>
          <v-card slot-scope="{ hover }" :class="`elevation-${hover ? 8 : 2}`">
            <v-card>
              <v-layout column justify-center align-center>
                <v-avatar size="256" tile class="margin10">
                  <v-img :src="avatarUrl"></v-img>
                </v-avatar>
                <v-flex>
                  <p class="display-3 font-weight-thin">{{clubName}}</p>
                </v-flex>
              </v-layout>
            </v-card>

            <v-card-title class="cardTitle">
              <v-layout column justify-center align-center>
                <v-flex>
                  <v-layout column justify-center align-center>
                    <v-layout column justify-start class>
                      <v-layout row align-center>
                        <v-icon class="margin10">person</v-icon>
                        <span class="font-weight-bold">社团负责人:</span>
                        <span class="font-weight-bold">{{clubCoordinator}}</span>
                      </v-layout>
                      <v-layout row align-center>
                        <v-icon class="margin10">email</v-icon>
                        <span class="font-weight-bold">{{userEmail}}</span>
                      </v-layout>
                      <v-layout row align-center class>
                        <v-icon class="margin10">phone</v-icon>
                        <span class="font-weight-bold">{{userTelephone}}</span>
                      </v-layout>
                    </v-layout>
                  </v-layout>
                </v-flex>

                <v-flex>
                  <br>
                  <p>{{userSelfIntrodction}}</p>
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
      </v-flex>
    </v-layout>
  </v-container>
</template>
<script>
export default {
  data: () => ({
    clubName: "学生电视中心",
    clubCoordinator: "赵四",
    wallpaperUrl: "http://upload.art.ifeng.com/2017/0425/1493105660290.jpg",
    avatarUrl:
      "http://img.touxiangzhan.com/upload/image/4a1490838412n2103307902t15.jpg",
    userNickName: "赵四",
    userRealName: "尼古拉斯",
    userEmail: "nkolas@zhao4.com",
    userTelephone: "13223456543",
    userSelfIntrodction:
      "这是尼古拉斯·赵四！尼古拉斯赵四是世界著名的舞蹈艺术家！著名的蹬腿舞就是由他所创。蹬腿舞以抽搐，两腿乱蹬，目光呆滞，五指伸直为特点，完美的体现了癫痫式的美感！如今，蹬腿舞者已经遍布世界各地。在贫困的非洲大地，缺少娱乐设施的贫穷儿童和少年们，平时就以蹬腿舞为娱乐活动，在某种程度上，蹬腿舞给他们带来的并不只是娱乐，而在精神上给予极大的鼓舞。所以尼古拉斯赵四的贡献是巨大的。舞蹈界第一人！所以说亚洲舞王这个称号还不能概括他为整个世界做出的贡献。如果一定要给他一个称号，我觉得应该是:宇宙舞王！！！！"
  })
};
</script>
<style>
.cardTitle {
  margin-top: 0px;
}
.margin10 {
  margin: 5px;
}
</style>
