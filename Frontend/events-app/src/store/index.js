import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex);

export default new Vuex.Store({
  state: {
    userId: "",
    username: "",
    userTitle: ""
  },
  mutations: {
    setUserId(state, userId){
      state.userId = userId
    },
    setUsername(state, username){
      state.username = username
    },
    setUserTitle(state, userTitle){
      state.userTitle = userTitle
    }
  },
  actions: {

  },
  getters: {

  }
})

