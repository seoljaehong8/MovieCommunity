<template>
  <div class='container'>
    <div class="row">
      <div class="offset-2 col-3">
        <img :src="moviePosterPath" alt="">
      </div>
      <div class="col-5">
        <h1>{{ movieTitle }}</h1>
        <h2>작성자 : {{ username }}</h2>
        <h2>작성시간 : {{ review.created_at }}</h2>
        <h2>수정시간 : {{ review.updated_at }}</h2>
      </div>
      <div class="row">
        <div class="col">
          <h2>내용 : {{ review.content }}</h2>
        </div>
      </div>
    </div>
    <hr>
  </div>
</template>

<script>
import axios from "axios"
import jwt_decode from "jwt-decode"

const SERVER_URL = process.env.VUE_APP_SERVER_URL

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
    console.log(this.review)

    // 토큰정보로 username 가져오기
    const token = localStorage.getItem('jwt')
    const decoded = jwt_decode(token);
    this.username = decoded.username

    // 영화상세 정보 가져오기
    const moviePk = this.review.movie
    axios({
      method: 'GET',
      url: `${SERVER_URL}/movies/${moviePk}`
    })
      .then(res => {
        this.moviePosterPath = `https://image.tmdb.org/t/p/w200${res.data.poster_path}`
        this.movieTitle = res.data.title
      })
  }
  
}
</script>

<style>

</style>