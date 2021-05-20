<template>
  <div>
    <ReviewListItem v-for="(review,idx) in reviewObj" :key="idx"
      :review="review" />
  </div>
</template>

<script>
import axios from 'axios'
import ReviewListItem from '@/components/reviews/ReviewListItem.vue'

const SERVER_URL = process.env.VUE_APP_SERVER_URL

export default {
  name: 'ReviewList',
  components: {
    ReviewListItem,
  },
  data: function() {
    return {
      reviewObj: null,
    }
  },
  created: function() {
    axios({
      method: 'GET',
      url: `${SERVER_URL}/reviews/`,
    })
      .then(res => {
        this.reviewObj = res.data
      })
  }

}
</script>

<style>

</style>