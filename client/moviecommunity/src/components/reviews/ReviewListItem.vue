<template>
  <div class="container" style="cursor: pointer;" @click="routeDetailPage(review)">
    <div class="row">
      <div class="offset-2 col-3">       
        <p class="movie-title">{{ movieTitle }}</p>
        <br>
        <a class="content-summury review-title">{{review.title}}</a>       
        <p class="content-summury review-content animate__animated animate__fadeInLeft">{{review.content}}</p>
        <p class="writer">작성자 : {{ username }}</p>        
        <!-- <p>작성시간 : {{ review.created_at | moment('YYYY-MM-DD HH:mm:ss') }}</p> -->
        <p class="date">{{ review.updated_at | moment('YYYY-MM-DD HH:mm:ss') }}</p>
      </div>
      
      <div class="col-5">
        <img :src="moviePosterPath" alt="">
      </div>

      <hr>  
    </div>
  </div>   
  
</template>

<script>
// import axios from "axios"
import Vue from 'vue' 
import vueMoment from 'vue-moment' 
Vue.use(vueMoment)


// const SERVER_URL = process.env.VUE_APP_SERVER_URL

export default {
  name: 'ReviewListItem', 

  props: {
    review: Object,
    key: Number
  },
  data: function() {
    return {
      moviePosterPath: null,
      movieTitle: null,
      username: null,
      selectedReview: null,
      test: '',
    }    
  },
  created: function() {
    this.test = 'abcdef'
    // 영화제목, 포스터이미지 정보 가져오기
    const moviePk = this.review.movie_id
    const movie = this.$store.state.movies[moviePk-1]

    this.moviePosterPath = `https://image.tmdb.org/t/p/w200${movie.poster_path}`
    this.movieTitle = movie.title
    this.username = this.review.username
  },
  methods: {
    routeDetailPage: function(review) {
      this.$router.push({name: 'ReviewDetail', 
        params: {
          review: review, 
          movietitle: this.movieTitle, 
          poster_path: this.moviePosterPath
        }
      })
    }
  }

  
}
</script>

<style>
.movie-title {
  font-size: x-large;
  text-align: left;
}

.content-summury {
  overflow: hidden;
  text-overflow: ellipsis;
  white-space: nowrap;
}

.review-title {
  font-size: x-large;
  text-decoration: underline;

}

.review-content {
  color: white;
  /* animation:  bounce;
  animation-duration: 2s;
  --animate-repeat: 2; */
}

.writer {
  /* display: inline-block; */
  text-align: right;
}

.date {
  /* display: inline-block; */
  text-align: right;
}


</style>