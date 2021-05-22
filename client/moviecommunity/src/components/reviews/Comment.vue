<template>
  <div>
    <h1>댓글</h1>
    <input v-model="content" type="text">
    <button @click="createComment">작성</button>
    <div v-for="(comment, idx) in comments" :key="idx">
      <li>{{comment.content}}</li>
    </div>
  </div>
</template>

<script>
import axios from 'axios'
import jwt_decode from "jwt-decode"

const SERVER_URL = process.env.VUE_APP_SERVER_URL


export default {
  name: 'Comment',
  props: {
    reviewId: Number,
  },
  data: function() {
    return {
      content: null,
      comments: null,
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
    createComment: function() {     
      const token = localStorage.getItem('jwt')
      const decoded = jwt_decode(token);

      const data = {
        content: this.content,
        username: decoded.username
      } 
      axios({
        method: 'POST',
        url: `${SERVER_URL}/reviews/comment/${this.reviewId}/`,
        headers: this.setToken(),
        data: data
      })
        .then(res => {
          console.log(res)
        })
        .catch(err => {
          console.log(err)
        })
    }
  },
  created: function() {
    console.log('코멘트 리뷰아이디:',this.reviewId)
    axios({
      method: 'GET',
      url: `${SERVER_URL}/reviews/comment/${this.reviewId}/`,
      headers: this.setToken(),
    })
      .then(res=>{
        this.comments = res.data
        console.log(res)
      })
      .catch(err => {
        console.log(err)
      })
  }
}
</script>

<style>

</style>