<template>
  <div class="container">
    <h1> MOVIE </h1>
    <div class="row">
      <MovieListItem 
        v-for="(movie,idx) in movies" 
        :key="idx"
        :movie="movie"/>
    </div>    
  </div>
</template>


<script>
import MovieListItem from '@/components/movies/MovieListItem.vue'
import axios from 'axios'
import { mapState } from 'vuex'


const SERVER_URL = process.env.VUE_APP_SERVER_URL

export default {
  name: 'MovieList',
  components: {
    MovieListItem,
    // PaginationItem,
  },
  computed: {
    ...mapState([
      'movies',
    ])
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
      url: `${SERVER_URL}/movies/`,
      headers: this.setToken()
    })
      .then(res => {
        this.$store.dispatch('createMovieList', res.data)
      })
      .catch(res => {
        console.log(res)
      })
  }
}
</script>

<style>

</style>