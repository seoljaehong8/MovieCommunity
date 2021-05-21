<template>
  <div class='container'>
    <router-link :to="{ name: 'ReviewListDetail' }" class="">
      <div class="row">

        <div class="offset-2 col-3">
          <img :src="moviePosterPath" alt="">
        </div>

        <div class="col-5">
          <h1>{{ movieTitle }}</h1>
          <!-- <h2>작성자 : {{ username }}</h2> -->
          <p>작성시간 : {{ review.created_at | moment('YYYY-MM-DD HH:mm:ss') }}</p>
          <p>수정시간 : {{ review.updated_at | moment('YYYY-MM-DD HH:mm:ss') }}</p>
        </div>

        <div class="row">
          <div class="col">
            <h2>제목 : {{ review.title }}</h2>
            <h2 class="content-summury">내용 : {{ review.content }}</h2>
          </div>
        </div>

        <!-- <div class="review">
          <p>리뷰 : {{ review.content }}</p>
          <p>작성자 : {{ username }}</p>
          <p>최종 작성 시간 : {{ review.updated_at }}</p>
        </div>  -->
      <hr>  
      </div>
    </router-link>
    <ReviewListDetail :review="review" />
  </div>  
  
</template>

<script>
// import axios from "axios"
import Vue from 'vue' 
import vueMoment from 'vue-moment' 
Vue.use(vueMoment)

import ReviewListDetail from '@/components/reviews/ReviewListDetail.vue'


// const SERVER_URL = process.env.VUE_APP_SERVER_URL

export default {
  name: 'ReviewListItem', 
  components: {
    ReviewListDetail
  },
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

.content-summury {
  overflow: hidden;
  text-overflow: ellipsis;
  white-space: nowrap;
}




</style>