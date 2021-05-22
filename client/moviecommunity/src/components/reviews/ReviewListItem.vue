<template>
  <div class="container" style="cursor: pointer;" @click="routeDetailPage(review)">
    <div class="row">
      <div class="offset-2 col-3">
        <img :src="moviePosterPath" alt="">
      </div>
      <div class="col-5">
        <h1>{{ review.movie_title }}</h1>
        <h2>작성자 : {{ review.user_name }}</h2>        
        <h2>작성시간 : {{ review.created_at | moment('YYYY-MM-DD HH:mm:ss') }}</h2>
        <h2>수정시간 : {{ review.updated_at | moment('YYYY-MM-DD HH:mm:ss') }}</h2>
        <h2>제목 : {{review.title}}</h2>
        <h2>내용 : {{review.content}}</h2>
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
  created: function() {
    this.moviePosterPath = `https://image.tmdb.org/t/p/w200${this.review.poster_path}`
  },
  methods: {
    routeDetailPage: function(review) {
      localStorage.setItem(`reviewId`, review.id)
      this.$router.push({name: 'ReviewDetail'})
    },    
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