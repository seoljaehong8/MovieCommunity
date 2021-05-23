<template>
  <div>
    <h1>Rating</h1>
    <RatingForm :movie="movie"/>    
    <RatingListItem v-for="(rating,idx) in getRating" 
      :key="idx"
      :rating="rating"
    />
  </div>
</template>

<script>
import RatingForm from '@/components/ratings/RatingForm.vue'
import RatingListItem from '@/components/ratings/RatingListItem.vue'

export default {
  name: "RatingOfMovie",
  props: {
    movie: Object,
  },
  components: {
    RatingForm,
    RatingListItem
  },
  computed: {
    getRating: function() {
      return this.movie.rating_set
    }
  },
  created: function() {
    console.log(this.movie)
  }
};
</script>

<style>
</style>