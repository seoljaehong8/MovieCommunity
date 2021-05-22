<template>
   <div class="container">
    <div class="row">

      <div class="offset-2 col-3">
        <img :src="posterPath" alt="">
      </div>
      <div class="col-5">

        <h1>{{ movieTitle }}</h1>
        <h2>제목 : {{review.title}}</h2>
        <h2>내용 : {{review.content}}</h2>
        <h2>작성자 : {{ review.username }}</h2>        
        <h2>작성시간 : {{ review.created_at | moment('YYYY-MM-DD HH:mm:ss') }}</h2>
        <h2>수정시간 : {{ review.updated_at | moment('YYYY-MM-DD HH:mm:ss') }}</h2>
      </div>

      <hr>  
    </div>
  </div>   

</template>

<script>
import Vue from 'vue' 
import vueMoment from 'vue-moment' 
Vue.use(vueMoment)

export default {
  name: 'ReviewDetail',
  data: function() {
    return {
      review: null,
      movieTitle: null,
      posterPath: null,
    }
  },
  
  created: function() {
    this.review = this.$route.params.review
    this.movieTitle = this.$route.params.movietitle
    this.posterPath = this.$route.params.poster_path
  }

  
}
</script>

<style>
  

</style>