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
    CREATE_MOVIE_LIST: function (state, movieList) {
      state.movies = movieList
    },
    CREATE_REVIEW_LIST: function (state, reviewList) {
      state.reviews = reviewList
    },
    CREATE_REVIEW: function (state, review) {
      state.reviews.push(review)
    },
    UPDATE_REVIEW: function (state, payload) {
      state.reviews[payload.index] = payload.review
    }
  },
  actions: {
    createMovieList: function ({ commit }, movieList) {
      commit("CREATE_MOVIE_LIST", movieList)
    },
    createReviewList: function ({ commit }, reviewList) {
      commit("CREATE_REVIEW_LIST", reviewList)
    },
    createReview: function ({ commit }, review) {
      commit("CREATE_REVIEW", review)
    },
    updateReview: function (context, payload) {
      const reviewId = payload.reviewId
      const updateTitle = payload.updateTitle
      const updateContent = payload.updateContent
      const review = context.state.reviews.find(review => review.id === reviewId)
      const index = context.state.reviews.indexOf(review)
      review.title = updateTitle
      review.content = updateContent

      context.commit("UPDATE_REVIEW", { review: review, index: index })
    }
  },
  getters: {
    getDetailReview: (state) => (reviewId) => {
      console.log('getters')
      return state.reviews.find(review => review.id === Number(reviewId))
    }
  },
  modules: {
  }
})
