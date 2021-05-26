<template>
  <div v-if="review" class="container">
    <div class="row">
      <div class="offset-3 col-2">
        <img :src="posterPath" alt="" />
      </div>
      <div class="col-4">
        <div class="row" style="color:lightgray">
          <h1>{{ review.movie_title }}</h1>
        </div>
        <div id="review-info" class="row">
          <p class="info">작성자 : {{ review.user_name }}</p>
          <p class="info">
            작성시간 : {{ review.created_at | moment("YYYY-MM-DD HH:mm:ss") }}
          </p>
          <p class="info">
            수정시간 : {{ review.updated_at | moment("YYYY-MM-DD HH:mm:ss") }}
          </p>
          <div v-if="isMine" class="offset-6 col-3">
            <button class="btn btn-outline-info" @click="changeIsUpdate">수정</button>
          </div>
          <div v-if="isMine" class="col-3">
            <button class="btn btn-outline-danger" @click="deleteReview">삭제</button>
          </div>
        </div>
        <br>        
      </div>
      <hr>
    </div>
    <div class="row">
      <div class="col">
        <div v-if="isUpdate">
          <textarea cols="50" rows="2" v-model="updateTitle" type="text"></textarea>
          <br>
          <textarea cols="50" rows="10" v-model="updateContent" type="text"></textarea>
          <br />
          <button @click="updateReview" class="btn btn-outline-info">수정완료</button>
        </div>
        <div v-else>
          <div v-if="isMine" class="review-detail">
            <h2 class="review-title">{{ review.title }}</h2>
            <p>{{ review.content }}</p>            
          </div>
          <div v-else class="review-detail">
            <h2 class="review-title">{{ review.title }}</h2>
            <h2>{{ review.content }}</h2>
          </div>
        </div>
      </div>
    </div>
    <hr>
    <CommentList :reviewId="this.review.id" />
  </div>
</template>

<script>
import jwt_decode from 'jwt-decode'

import axios from "axios";
import CommentList from "@/components/comments/CommentList.vue";

const SERVER_URL = process.env.VUE_APP_SERVER_URL;

const token = localStorage.getItem('jwt')
let username = ''
if (token){
  const decoded = jwt_decode(token)
  username = decoded.username
} else{
  username = 'user'
}

export default {
  name: "ReviewDetail",
  data: function () {
    return {
      review: null,
      posterPath: null,
      isUpdate: false,
      updateTitle: null,
      updateContent: null,
      reivews: null,
    };
  },
  components: {
    CommentList,
  },
  computed: {
    isMine: function() {
      return username === this.review.user_name
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
    updateReview: function () {
      const data = {
        username: this.review.user_name,
        title: this.updateTitle,
        content: this.updateContent,
        movie: this.review.movie_id,
      };
      const payload = {
        review: this.review,
        updateTitle: this.updateTitle,
        updateContent: this.updateContent,
      };
      this.$store.dispatch("updateReview", payload);
      this.isUpdate = false;
      const reviewId = this.review.id;
      axios({
        method: "PUT",
        url: `${SERVER_URL}/reviews/${reviewId}/`,
        headers: this.setToken(),
        data: data,
      })
        .then((res) => {
          alert('글이 수정 되었습니다.')
          console.log(res);
        })
        .catch((err) => {
          console.log(err);
        });
    },
    deleteReview: function () {
      const reviewId = this.review.id;
      // this.$store.dispatch("deleteReview", this.review);
      axios({
        method: "DELETE",
        url: `${SERVER_URL}/reviews/${reviewId}/`,
        headers: this.setToken(),
      })
        .then((res) => {
          alert("글이 삭제 되었습니다.");
          this.$router.push({ name: "ReviewList" });
          console.log(res);
        })
        .catch((err) => {
          console.log(err);
        });
    },
    changeIsUpdate: function () {
      this.isUpdate = true;
    },
  },
  created: function () {
    const reviewId = localStorage.getItem("reviewId");
    axios({
      method: "GET",
      url: `${SERVER_URL}/reviews/${reviewId}/`,
      headers: this.setToken(),
    })
      .then((res) => {
        this.review = res.data;
        this.updateTitle = this.review.title;
        this.updateContent = this.review.content;
        this.posterPath = `https://image.tmdb.org/t/p/w200${this.review.poster_path}`;
        console.log(res);
      })
      .catch((err) => {
        console.log(err);
      });
  },
};
</script>

<style scoped>

.info {
  text-align: right;
}

.review-detail {
    margin: 0 auto;
    width: 800px;
    padding: 30px 90px;
    border-radius: 30px;
    /* background-color: #F6F6F6; */
    background-color: #e6e6e6;
    font-family: 'Noto Sans KR', sans-serif;
    color: black;
}
#review-info{
  margin-top:120px;
}

.offset-6 {
  padding-left:50px;
  padding-right:0px;
}

.offset-6 > .col-3 {
  padding: 0px;
}

.review-title{
  text-decoration: underline;
  font-style: italic;
  margin-bottom: 30px;
}
textarea{
  border-radius: 10px;
  background-color: #f3f3f3;
  padding: 10px 10px;
}

</style>