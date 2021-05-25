<template>
  <div>
    <div class="comment-username">
      작성자 : {{ comment.user_name }} 
    </div>
    <div class="comment-content">
      {{ comment.content }} 
    </div>
    {{ comment.created_at | moment("YYYY-MM-DD HH:mm:ss") }} |
    {{ comment.updated_at | moment("YYYY-MM-DD HH:mm:ss") }}
    <button class="btn btn-outline-info" v-if="isMine" @click="deleteComment">삭제</button>  
    <hr>
  </div>
</template>

<script>
import axios from "axios";
import jwt_decode from 'jwt-decode'

const token = localStorage.getItem('jwt')
let username = ''
if (token){
  const decoded = jwt_decode(token)
  username = decoded.username
} else{
  username = 'user'
}

const SERVER_URL = process.env.VUE_APP_SERVER_URL;

export default {
  name: 'CommentListItem',
  props: {
    comment: Object,
    reviewId: Number,
  },
  computed: {
    isMine: function() {
      return username === this.comment.user_name
    }
  },
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

<style scoped>
  .comment-username {
    margin-right: 250px;
  }

  .comment-content {
    font-weight: 600;
    font-size: large;
  }
</style>