<template>
  <div class="container">
    <h1>MOVIE</h1>
    <div class="row">
      <MovieListItem 
        v-for="(movie,idx) in movieObj" 
        :key="idx"
        :movie="movie"/>
    </div>
  </div>
</template>

<script>
import axios from 'axios'
import MovieListItem from '@/components/movies/MovieListItem.vue'

const SERVER_URL = process.env.VUE_APP_SERVER_URL

export default {
  name: 'MovieList',
  components: {
    MovieListItem,
  },
  data: function() {
    return {
      movieObj: {

      }
    }
  },
  created: function() {
    axios({
      method: 'get',
      url: `${SERVER_URL}/movies`
    })
      .then(res => {
        this.movieObj = res.data
      })
  }
}
</script>

<style>

</style>