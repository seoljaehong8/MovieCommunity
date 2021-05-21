<template>
  <div>
    <h1>Review Form</h1>
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
      title: null,
      content: null,
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
        movie: 1
      }
      axios({
        method: 'POST',
        url: `${SERVER_URL}/reviews/`,
        headers: this.setToken(),
        data: data,
      })
        .then(res => {
          console.log(res)
        })
        .catch(err => {
          console.log(err)
        })
    }
  }
}
</script>

<style>

</style>