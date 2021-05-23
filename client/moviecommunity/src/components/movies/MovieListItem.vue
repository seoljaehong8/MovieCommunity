<template>
  <div class="card col-xl-4 col-12 my-3" @click="movieDetail" style="cursor:pointer;">
    <img :src="getPosterUrl" class="card-img-top" alt="...">
    <div class="card-body">
      <div class="star-ratings">
        <div 
          class="star-ratings-fill space-x-2 text-lg"
          :style="{ width: ratingToPercent + '%' }"
        >
          <span>★</span><span>★</span><span>★</span><span>★</span><span>★</span>
        </div>
        <div class="star-ratings-base space-x-2 text-lg">
          <span>★</span><span>★</span><span>★</span><span>★</span><span>★</span>
        </div>
      </div>

      <h5 class="card-title">{{ this.movie.title }}</h5>
      <p class="card-text">{{ this.movie.overview }}</p>
    </div>
  </div>

</template>

<script>
export default {
  name: 'MovieListItem',
  props: {
    movie: Object,
  },
  computed: {
    getPosterUrl: function() {
      const url = `https://image.tmdb.org/t/p/w500${this.movie.poster_path}`
      return url    
    },
    ratingToPercent: function() {
      const score = this.movie.vote_average * 10;
      return score + 1.5;
    }
  },
  methods: {
    movieDetail: function() {
      localStorage.setItem(`movieId`, this.movie.id)
      console.log(this.movie.id)
      this.$router.push({name:'movieDetail'})
    }
  }
}
</script>

<style>
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
</style>