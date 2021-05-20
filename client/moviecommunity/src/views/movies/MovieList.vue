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
import MovieListItem from '@/components/MovieListItem.vue'

const url = 'http://127.0.0.1:8000/'

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
      url: `${url}movies`
    })
      .then(res => {
        this.movieObj = res.data
      })
  }
}
</script>

<style>

</style>