import Vue from "vue";
import Vuex from "vuex";

Vue.use(Vuex);

export default new Vuex.Store({
  state: {
    snackbar: {
      show: true,
      color: "green",
      text: "正在加载"
    },
    loading: {
      show: true,
      color: "",
    },
    club_url: "",
    interview: [{
      url: "",
      pk: 14,
      title: "",
      description:
        "",
      edit_finish: true,
      is_public: true,
      interviewTimeline: [{
        url: "",
        pk: 0,
        interview: "",
        location: "",
        date: "",
        remarks: ""
      }]
    },],
    memberships: []
  },
  mutations: {
    initializeInterview(state, club_url: string) {
      state.club_url = club_url
      console.log('in initialInterview')
      if (!club_url) {
        console.error("club_url is empty")
        return
      }
      Vue.axios
        .get(state.club_url + "interview/")
        .then((response: any) => {
          state.interview = response.data
        })
        .finally(() => { });
    },
    initializeMemberships(state) {
      if (!state.club_url) {
        return
      }
      Vue.axios.get(state.club_url + 'membership/')
        .then(({ data }) => {
          state.memberships = data
        })
    },
    popSuccess(state, text: string = '') {
      if (!text) {
        text = "操作成功"
      }
      state.snackbar = {
        show: true,
        text,
        color: "green",
      }
    },
    popError(state, text = '') {
      if (!text) {
        console.log(text)
        text = "发生异常"
      }
      state.snackbar = {
        show: true,
        color: "red",
        text
      }
    }
  },
  actions: {}
});
