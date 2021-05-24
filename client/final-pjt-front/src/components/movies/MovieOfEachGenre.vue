<template>
  <div>
    <h1 class="text-start" style="color:white;"> {{genre}} </h1>
    <div>
      <carousel :items="8" :nav="true" :dots="false" class="marginTop50">
        <div v-for="(movie,idx) in movies" :key="idx">
          <div class="card" @click="movieDetail(movie)" style="cursor:pointer; height:350px; background-color:black;">
            <img :src="getPosterUrl(movie)" class="card-img-top" alt="...">
            <!-- <div class="card-body">
              <h5 class="card-title">{{ movie.title }}</h5>
              <div class="star-ratings mx-auto">
                <div 
                  class="star-ratings-fill space-x-2 text-lg"
                  :style="{ width: ratingToPercent(movie) + '%' }"
                >
                  <span>★</span><span>★</span><span>★</span><span>★</span><span>★</span>
                </div>
                <div class="star-ratings-base space-x-2 text-lg">
                  <span>★</span><span>★</span><span>★</span><span>★</span><span>★</span>
                </div>
              </div>              
            </div> -->
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
      this.$router.push({name:'movieDetail'})
    }
  },
  created: function() {
    this.movies = this.$store.getters.getMovieOfGenre(this.genre).slice(0,30)
  },
}
</script>

<style>

</style>