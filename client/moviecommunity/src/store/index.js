import Vue from 'vue'
import Vuex from 'vuex'
import createPersistedState from "vuex-persistedstate"

Vue.use(Vuex)

export default new Vuex.Store({
  plugins: [
    createPersistedState(),
  ],
  state: {
    movies: [],
    reviews: [],
  },
  mutations: {
    CREATE_MOVIE_LIST: function(state, movieList) {
      state.movies = movieList
    },
    CREATE_REVIEW_LIST: function(state, reviewList){
      state.reviews = reviewList
    }
  },
  actions: {
    createMovieList: function({commit}, movieList) {
      commit("CREATE_MOVIE_LIST", movieList)
    },
    createReviewList: function({commit}, reviewList) {
      commit("CREATE_REVIEW_LIST", reviewList)
    }
  },
  getters: {

  },
  modules: {
  }
})
