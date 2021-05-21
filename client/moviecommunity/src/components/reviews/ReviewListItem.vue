<template>
  <div class="container">
    <div class="row">
      <div class="offset-2 col-3">
        <img :src="moviePosterPath" alt="">
      </div>
      <div class="col-5">
        <h1>{{ movieTitle }}</h1>
        <h2>작성자 : {{ username }}</h2>        
        <h2>작성시간 : {{ review.created_at | moment('YYYY-MM-DD HH:mm:ss') }}</h2>
        <h2>수정시간 : {{ review.updated_at | moment('YYYY-MM-DD HH:mm:ss') }}</h2>
      </div>
      <div class="row">
        <div class="col">
          <h2>제목 : {{ review.title }}</h2>
          <h2>내용 : {{ review.content }}</h2>
        </div>
      </div>
      <div class="review">
        <p>리뷰 : {{ review.content }}</p>
        <p>작성자 : {{ username }}</p>
        <p>최종 작성 시간 : {{ review.updated_at }}</p>
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
  },
  data: function() {
    return {
      moviePosterPath: null,
      movieTitle: null,
      username: null,
    }    
  },
  created: function() {

    // 영화제목, 포스터이미지 정보 가져오기
    const moviePk = this.review.movie_id
    const movie = this.$store.state.movies[moviePk-1]

    this.moviePosterPath = `https://image.tmdb.org/t/p/w200${movie.poster_path}`
    this.movieTitle = movie.title
    this.username = this.review.username
  }
  
}
</script>

<style>

.posterpath {
  /* text-align: center; */
  float: left;

}

.review {
  /* display:inline-block; */
  float: none;



}

</style>