<template>
  <div v-if="review" class="container">
    <div class="row">
      <div class="offset-2 col-3">
        <img :src="posterPath" alt="" />
      </div>
      <div class="col-5">
        <h1>영화제목 : {{ review.movie_title }}</h1>
        <h2>작성자 : {{ review.user_name }}</h2>
        <h2>
          작성시간 : {{ review.created_at | moment("YYYY-MM-DD HH:mm:ss") }}
        </h2>
        <h2>
          수정시간 : {{ review.updated_at | moment("YYYY-MM-DD HH:mm:ss") }}
        </h2>
        <div v-if="isUpdate">
          <input v-model="updateTitle" type="text" />
          <input v-model="updateContent" type="text" />
          <br />
          <button @click="updateReview">수정</button>
        </div>
        <div v-else>
          <h2>글 제목 : {{ review.title }}</h2>
          <h2>내용 : {{ review.content }}</h2>
          <button @click="changeIsUpdate">수정</button>
          <button @click="deleteReview">삭제</button>
        </div>
      </div>

      <hr />
    </div>
    <CommentList :reviewId="this.review.id" />
  </div>
</template>

<script>
import Vue from "vue";
import vueMoment from "vue-moment";
import axios from "axios";

import CommentList from "@/components/comments/CommentList.vue";

Vue.use(vueMoment);
const SERVER_URL = process.env.VUE_APP_SERVER_URL;

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
      this.$store.dispatch("deleteReview", this.review);
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

<style>
</style>