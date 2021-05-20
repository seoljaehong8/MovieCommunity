<template>
  <div class="container">
    <h1> MOVIE </h1>
    <div class="row">
      <MovieListItem 
        v-for="(movie,idx) in movieObj" 
        :key="idx"
        :movie="movie"/>
    </div>
    <nav aria-label="Page navigation example">
      <ul class="pagination justify-content-center">
        <li class="page-item disabled">
          <a class="page-link" href="#" tabindex="-1" aria-disabled="true">Previous</a>
        </li>
      
      <PaginationItem
        v-for="idx in movieObj.length/10" 
        :key="idx"
        :pageNumber="idx"/>
 
        <li class="page-item">
          <a class="page-link" href="#">Next</a>
        </li>
      </ul>
    </nav>
  </div>
</template>

<script>
import axios from 'axios'
import MovieListItem from '@/components/movies/MovieListItem.vue'
import PaginationItem from '@/components/movies/PaginationItem.vue'

const SERVER_URL = process.env.VUE_APP_SERVER_URL

export default {
  name: 'MovieList',
  components: {
    MovieListItem,
    PaginationItem,
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