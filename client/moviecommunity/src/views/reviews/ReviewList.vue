<template>
  <div>
    <ReviewListItem v-for="(review,idx) in reviews" :key="idx"
      :review="review" />
  </div>
</template>

<script>
import axios from 'axios'
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
    ])
  },
  created: function() {
    axios({
      method: 'GET',
      url: `${SERVER_URL}/reviews/`,
    })
      .then(res => {
        this.$store.dispatch('createReviewList',res.data)
      })
  }

}
</script>

<style>

</style>