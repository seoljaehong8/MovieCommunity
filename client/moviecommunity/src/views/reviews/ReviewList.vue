<template>  
  <div>
    <div>
      <button type="button" class="btn btn-light">
        <router-link :to="{ name: 'ReviewForm' }" class="a-tag">리뷰 작성</router-link>
      </button>

    </div>
    <div class="review-list">
      <ReviewListItem v-for="(review,idx) in reviews" 
      :key="idx"
      :review="review" />
    </div>
  </div>
</template>

<script>
import axios from 'axios'
// import _ from 'lodash'
import { mapState } from 'vuex'

import ReviewListItem from '@/components/reviews/ReviewListItem.vue'

const SERVER_URL = process.env.VUE_APP_SERVER_URL

export default {
  name: 'ReviewList',
  components: {
    ReviewListItem,
  },
  computed: {
    ...mapState([
      'reviews'
    ]),
  },
  methods: {
    setToken: function () {
      const token = localStorage.getItem('jwt')
      const config = {
        Authorization: `JWT ${token}`
      }
      return config
    },
  },
  created: function() {    
    axios({
      method: 'GET',
      url: `${SERVER_URL}/reviews/`,
      headers: this.setToken()
    })
      .then(res => {
        this.$store.dispatch('createReviewList',res.data)
      })
      .catch(err => {
        console.log(err)
      })
  }
}
</script>

<style>
  .a-tag{
    text-decoration: none;
  }

  .review-list {
    margin-top: 50px;
  }
</style>