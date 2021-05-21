<template>
  <div>
    <button type="button" class="btn btn-primary" data-bs-toggle="modal" data-bs-target="#exampleModal">
      영화선택
    </button>

    <div class="modal fade" id="exampleModal" tabindex="-1" aria-labelledby="exampleModalLabel" aria-hidden="true">
      <div class="modal-dialog">
        <div class="modal-content">
          <div class="modal-header">
            <h5 class="modal-title" id="exampleModalLabel">영화선택</h5>
            <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
          </div>
          <div class="modal-body">
            <input v-model="search" @keydown.enter="searchMovie" type="text" placeholder="movie_title">
            <button @click="searchMovie">검색</button>
            <br>
            <div v-for="(movie,idx) in movies" :key="idx">
              <div class="select-title" data-bs-dismiss="modal" @click="clickSelectTitle(movie)">
                <img :src="getMoviePosterUrl(movie)" width="100" alt="movieImg">
                {{ movie.title }}
              </div>
            </div>
          </div>
          <div class="modal-footer">
            <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">Close</button>
          </div>
        </div>
      </div>
    </div>
    <h1>Review Form</h1>
    <div v-if="selectedMovie">
      <img :src="getMoviePosterUrl(selectedMovie)" alt="">
      {{ selectedMovie.title }}
      {{ selectedMovie.id }}
    </div>
    
    <br>
    <input v-model="title" type="text" placeholder="title">
    <br>
    <input v-model="content" type="text" placeholder="content">
    <br>
    <button @click="createReview">작성</button>
  </div>
</template>


<script>
import axios from 'axios'
import jwt_decode from "jwt-decode"

const SERVER_URL = process.env.VUE_APP_SERVER_URL

export default {
  name: 'ReviewForm',
  data: function() {
    return {
      search: null,   // 모달에서 검색하는 input 내용
      title: null,    // 리뷰 작성시 글의 제목
      content: null,  // 리뷰 작성시 글의 내용
      movies: null,   // 전체 영화 목록
      selectedMovie: null,  // 검색에서 선택한 영화
    }
  },
  methods: {
    setToken: function () {
      const token = localStorage.getItem('jwt')
      const config = {
        Authorization: `JWT ${token}`
      }
      return config
    },
    createReview: function() {
      // 토큰정보로 username 가져오기
      const token = localStorage.getItem('jwt')
      const decoded = jwt_decode(token);
      
      const data = {
        username: decoded.username,
        title: this.title,
        content: this.content,
        movie: this.selectedMovie.id
      }
      axios({
        method: 'POST',
        url: `${SERVER_URL}/reviews/`,
        headers: this.setToken(),
        data: data,
      })
        .then(res => {
          console.log(res)
          // setTimeout(() => {
          //   this.$router.push({ name: 'ReviewList' })
          // },1000)
          alert('글이 작성 되었습니다.')
          this.$router.push({ name: 'ReviewList' })
        })
        .catch(err => {
          console.log(err)
        })    
    },
    // 검색어로 영화 찾기
    searchMovie: function() {
      this.movies = this.$store.state.movies.filter(movie => {
        return movie.title.includes(this.search)
      })
    },
    // 원하는 영화 선택하기
    clickSelectTitle: function(movie) {
      this.selectedMovie = movie
    },    
    // 선택한 영화 포스터 url 불러오기
    getMoviePosterUrl: function(movie) {
      const posterPath = movie.poster_path
      const url = `https://image.tmdb.org/t/p/w200${posterPath}`
      return url
    },

  },
}
</script>

<style scoped>
  .select-title {
    cursor: pointer;
  }
</style>