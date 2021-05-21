<template>
    <div>   
    
      <div class="posterpath">
        <p>{{ movieTitle }}</p>
        <img :src="moviePosterPath" alt="">       
      </div>
     
      <div class="review">
        <p>리뷰 : {{ review.content }}</p>
        <p>작성자 : {{ username }}</p>
        <p>최종 작성 시간 : {{ review.updated_at }}</p>
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

.posterpath {
  /* text-align: center; */
  float: left;

}

.review {
  /* display:inline-block; */
  float: none;



}

</style>