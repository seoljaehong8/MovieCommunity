<template>
  <div>
    <div v-if="movie">
      <h1>movieDetail</h1>
      <h1>제목 : {{ movie.title }}</h1>
      <img :src="getPosterUrl" alt="">
      <h3>개봉날짜 : {{ movie.release_date}}</h3>
      <h3>줄거리 : {{ movie.overview }}</h3>
      <h3>장르 : {{ movie.genre }}</h3>
      <h3>평점 : {{ movie.vote_average }}</h3>
      <h3>평점을 준 사람 : {{ movie.vote_count }}</h3>
    </div>
    <div>
      <button @click="clickRating">평점</button>
      <button @click="clickReview">리뷰</button>
    </div>
    <!-- 평점 보여주기 -->
    <div v-if="isRating && movie">
      <RatingOfMovie :movie="movie"/>
    </div>
    <!-- 리뷰 보여주기 -->
    <div v-if="isReview">
      <ReviewOfMovie v-for="(review,idx) in movie.review_set"
        :key="idx"
        :review="review"
      />
    </div>
  </div>
</template>

<script>
import axios from 'axios'
import ReviewOfMovie from '@/components/movies/ReviewOfMovie.vue'
import RatingOfMovie from '@/components/movies/RatingOfMovie.vue'

const SERVER_URL = process.env.VUE_APP_SERVER_URL;

export default {
  name: 'movieDetail',
  components:{
    ReviewOfMovie,
    RatingOfMovie
  },
  data: function() {
    return {
      movie: null,
      isRating: true,
      isReview: false,
    }
  },
  computed: {
    getPosterUrl: function() {
      const url = `https://image.tmdb.org/t/p/w500${this.movie.poster_path}`
      return url    
    },
  },
  methods: {
    setToken: function () {
      const token = localStorage.getItem("jwt");
      const config = {
        Authorization: `JWT ${token}`,
      };
      return config;
    },
    clickRating: function() {
      console.log('click rating')
      this.isReview = false
      this.isRating = true
      console.log(this.isReview,this.isRating)
    },
    clickReview: function() {
      console.log('click review')
      this.isReview = true
      this.isRating = false
      console.log(this.isReview,this.isRating)
    }
  },
  created: function(){
    const movieId = localStorage.getItem(`movieId`)
    axios({
      method: 'GET',
      url: `${SERVER_URL}/movies/${movieId}/`,
      headers: this.setToken()
    })
      .then(res => {
        this.movie = res.data
        console.log(res)
      })
      .catch(err => {
        console.log(err)
      })
  }
}
</script>

<style>

</style>