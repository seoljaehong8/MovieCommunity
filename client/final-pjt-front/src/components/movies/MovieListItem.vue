<template>
  <div>
    <h1 class="text-start" style="color:white;"> 인기순 </h1>
    <div>
      <carousel :items="8" :nav="true" :dots="false" class="marginTop50">
        <div v-for="(movie,idx) in movies" :key="idx">
          <div class="card" @click="movieDetail(movie)" style="cursor:pointer; height:350px; background-color:black;">
            <div id="hov">
              {{ movie.title }}
            </div>
            <img :src="getPosterUrl(movie)" class="card-img-top" id="image" alt="...">
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
  name: 'MovieListItem',
  components:{
    carousel
  },
  props: {
    movies: Array,
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
  }
}
</script>

<style scoped>
.star-ratings {
  color: #aaa9a9; 
  position: relative;
  unicode-bidi: bidi-override;
  width: max-content;
  -webkit-text-fill-color: transparent; /* Will override color (regardless of order) */
  -webkit-text-stroke-width: 1.3px;
  -webkit-text-stroke-color: #2b2a29;
}
 
.star-ratings-fill {
  font-size: 30px;
  color: #fff58c;
  padding: 0;
  position: absolute;
  z-index: 1;
  display: flex;
  top: 0;
  left: 0;
  overflow: hidden;
  -webkit-text-fill-color: gold;
}
 
.star-ratings-base {
  font-size: 30px;
  z-index: 0;
  padding: 0;
}

img:hover {
  transform:scale(1.5);
  /* transition: transform.3s; */
}

#hov {
  display: none;
}

#image.hover + #hov {
  display: inline;

}

</style>