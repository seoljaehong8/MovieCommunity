<template>
  <div>
    <div class="d-flex">
      <h1 @click="showAllMovies(genre)" style="color:white; cursor:pointer;"> {{genre}} </h1>
    </div>
    <div>
      <carousel :items="10" :nav="false" :dots="false" class="marginTop50">
        <div v-for="(movie,idx) in movies" :key="idx">
          <div class="card" @click="movieDetail(movie)">
            <img :src="getPosterUrl(movie)" class="card-img-top" alt="...">
          </div>          
        </div>
      </carousel>
    </div>    
  </div>
</template>

<script>
import carousel from 'vue-owl-carousel'

export default {
  name: 'MovieOfEachGenre',
  components:{
    carousel
  },
  props: {
    genre: String,
  },
  data: function() {
    return {
      movies: null,
    }
  },
  methods: {
    getPosterUrl: function(movie) {
      const url = `https://image.tmdb.org/t/p/w300${movie.poster_path}`
      return url    
    },
    ratingToPercent: function(movie) {
      const score = movie.vote_average * 10;
      return score + 1.5;
    },
    movieDetail: function(movie) {
      localStorage.setItem(`movieId`, movie.id)
      localStorage.setItem('movieTitle',movie.title)
      this.$router.push({name:'movieDetail'})
    },
    showAllMovies: function(genre) {
      localStorage.setItem('movieGenre',genre)
      this.$router.push({name:'ShowAllMovies'})
    }
  },
  created: function() {
    this.movies = this.$store.getters.getMovieOfGenre(this.genre).slice(0,30)
  },
}
</script>

<style scoped>
.card{
  cursor:pointer; 
  height:350px; 
  background-color:rgb(15, 15, 15);  
}
img:hover {
  transform:scale(1.2) translate(-22px,30px) !important;
  z-index:2;
}
</style>