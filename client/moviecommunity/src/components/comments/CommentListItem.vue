<template>
  <div>
    {{ comment.content }} | 
    {{ comment.user_name}} |
    {{ comment.created_at | moment("YYYY-MM-DD HH:mm:ss") }} |
    {{ comment.updated_at | moment("YYYY-MM-DD HH:mm:ss") }}
    <!-- <button v-if="isMine" @click="deleteComment">삭제</button>   -->
    <button  @click="deleteComment">삭제</button>  
  </div>
</template>

<script>
import axios from "axios";
// import jwt_decode from 'jwt-decode'

const SERVER_URL = process.env.VUE_APP_SERVER_URL;
// const token = localStorage.getItem('jwt')
// const decoded = jwt_decode(token)

export default {
  name: 'CommentListItem',
  props: {
    comment: Object,
    reviewId: Number,
  },
  // computed: {
  //   isMine: function() {
  //     return this.comment.user_name === decoded.username
  //   }
  // },
  methods: {
    setToken: function () {
      const token = localStorage.getItem("jwt");
      const config = {
        Authorization: `JWT ${token}`,
      };
      return config;
    },
    deleteComment: function() {
      console.log('comment.id : ',this.comment.id)
      this.$store.dispatch('deleteComment',this.comment)

      axios({
        method: "DELETE",
        url: `${SERVER_URL}/reviews/comment/${this.reviewId}/${this.comment.id}/`,
        headers: this.setToken()
      })
        .then(res => {
          console.log(res)
        })
        .catch(err => {
          console.log('123',err)
        })
    }
  }
} 
</script>

<style>

</style>