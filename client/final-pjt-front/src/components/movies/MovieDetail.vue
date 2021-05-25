<template>
  <div class="container">
    <div class="row">
      <MovieVideo :video="video"/>
    </div>
    <div class="row mb-5">
      <div id="info" @click="clickInfo" class="offset-1 col-2 align-self-center category" :class="{'category-background':isInfo}">영화정보</div>
      <div id="rating" @click="clickRating" class="col-2 align-self-center category" :class="{'category-background':isRating}">평점</div>
      <div id="review" @click="clickReview" class="col-2 align-self-center category" :class="{'category-background':isReview}">리뷰</div>
    </div>
    <div v-if="isInfo" class="row">
      <div class="col-6">
        <img :src="posterUrl" alt="">
      </div>
      <div class="col-6 text-start">
        <div v-if="movie" style="color:lightgray;">
          <h1 class="padding">제목 : {{movie.title}}</h1>
          <h3>줄거리 </h3> <br>
          <h5 class="padding"> {{ movie.overview }}</h5>
          <h3 class="padding">개봉날짜 : {{ movie.release_date}}</h3>
          <h3 class="padding">장르 : {{ movie.genre }}</h3>
          <h3 class="padding">평점 : {{ movie.vote_average }}</h3>
        </div>
      </div>
    </div>
    <div v-else-if="isRating" class="row">
      <RatingOfMovie :movie="movie"/>
    </div>    
    <div v-else-if="movie.review_set.length>0 && isReview" class="row">
      <span> 사용자 평점 총 {{movie.review_count}}건</span>
      <ReviewOfMovie v-for="(review,idx) in movie.review_set"
        :key="idx"
        :review="review"
      />
    </div>
    <div v-else>
      <h1 style="color:white; margin-top:100px;">등록된 리뷰가 없습니다.</h1>
      <router-link :to="{ name: 'ReviewList' }">리뷰쓰러가기</router-link>
    </div>
  </div>
</template>

<script>
import axios from 'axios'
import ReviewOfMovie from '@/components/movies/ReviewOfMovie.vue'
import RatingOfMovie from '@/components/movies/RatingOfMovie.vue'
import MovieVideo from '@/components/movies/MovieVideo.vue'

const SERVER_URL = process.env.VUE_APP_SERVER_URL;

const API_URL = 'https://www.googleapis.com/youtube/v3/search'
const API_KEY = process.env.VUE_APP_YOUTUBE_API_KEY

export default {
  name: 'movieDetail',
  components:{
    ReviewOfMovie,
    RatingOfMovie,
    MovieVideo
  },
  data: function() {
    return {
      movie: null,
      isInfo: true,
      isRating: false,
      isReview: false,
      video: null,
      posterUrl: null,
    }
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
      this.isRating = true
      this.isReview = false
      this.isInfo = false
      const info = document.querySelector('#rating')
      info.classList.add('category-background')
      console.log(this.isReview,this.isRating)
    },
    clickReview: function() {
      console.log('click review')
      this.isReview = true
      this.isRating = false
      this.isInfo = false
      const info = document.querySelector('#review')
      info.classList.add('category-background')
      console.log(this.isReview,this.isRating)
    },
    clickInfo: function() {
      this.isInfo = true
      this.isRating = false
      this.isreview = false
      const info = document.querySelector('#info')
      info.classList.add('category-background')
    },
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
        this.posterUrl = `https://image.tmdb.org/t/p/w300${res.data.poster_path}`
        console.log(res)
      })
      .catch(err => {
        console.log(err)
      })
    axios.get(API_URL,{
        params: {
          key: API_KEY,
          // key: 'AIzaSyAGkxTvvS55ycu7HecOY7nU9_eDpEN-3Vo',
          part: 'snippet',
          q: localStorage.getItem('movieTitle')+'예고',
          type: 'video',
        }
      })
        .then(res =>{
          console.log('youtube:',res.data)
          this.video = res.data.items.slice(0,1)
        })
        .catch(error => {
          console.log(error)
        })
  }
}
</script>

<style scoped>
  .padding {
    padding-bottom: 10px;;
  }
  .category {
    font-size: 30px;
    color: white;
    font-weight:400;
    border-radius: 12px;
    cursor: pointer;
  }
  .category:hover{
    background-color: gray;
  }
  .category-background {
    color: black;
    background-color:lightgray;
  }
  span{
  color:lightgray;
  font-size:20px;
  margin-left:80px;
  margin-bottom: 20px;
  text-align:left;
  }

</style>