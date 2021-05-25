<template>
  <div >
    <MovieListItem :movies="movies"/>  
    <MovieOfEachGenre v-for="(genre,idx) in genreList" 
    :key="idx"
    :genre="genre"/>
  </div>
</template>


<script>
import MovieListItem from '@/components/movies/MovieListItem.vue'
import MovieOfEachGenre from '@/components/movies/MovieOfEachGenre.vue'
import axios from 'axios'

const SERVER_URL = process.env.VUE_APP_SERVER_URL

export default {
  name: 'MovieList',
  components: {
    MovieListItem,
    MovieOfEachGenre
    // PaginationItem,
  },
  computed: {
    movies: function() {
      return this.$store.getters.getMovieList.slice(0,30)
    },
    genreList: function() {
      const genreList = [
        '액션','어드벤처','애니메이션','범죄','다큐멘터리','드라마',
        '가족','판타지','역사','공포','음악','미스테리','로맨스',
        'SF','스릴러','전쟁','서부'
      ]
      return genreList
    }
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