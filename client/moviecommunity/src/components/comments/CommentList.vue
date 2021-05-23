<template>
  <div>
    <h1>댓글</h1>
    <input v-model="content" @keydown.enter="createComment" type="text" />
    <button @click="createComment">작성</button>
    <CommentListItem v-for="(comment, idx) in comments" :key="idx"
      :comment="comment"
      :reviewId="reviewId"/>
  </div>
</template>

<script>
import CommentListItem from '@/components/comments/CommentListItem.vue'
import axios from "axios";
import _ from "lodash";

const SERVER_URL = process.env.VUE_APP_SERVER_URL;

export default {
  name: "Comment",
  props: {
    reviewId: Number,
  },
  components: {
    CommentListItem,
  },
  data: function () {
    return {
      content: null,
    };
  },
  computed: {
    comments: function () {
      return _.orderBy(
        this.$store.getters.getComments,
        ["created_at"],
        ["desc"]
      );
    },
  },
  methods: {
    setToken: function () {
      const token = localStorage.getItem("jwt");
      const config = {
        Authorization: `JWT ${token}`,
      };
      return config;
    },
    createComment: function () {
      const data = {
        content: this.content,
      };
      axios({
        method: "POST",
        url: `${SERVER_URL}/reviews/comment/${this.reviewId}/`,
        headers: this.setToken(),
        data: data,
      })
        .then((res) => {
          this.$store.dispatch("createComment", res.data);
          console.log(res);
        })
        .catch((err) => {
          console.log(err);
        });
        this.content = ''
    },
  },
  created: function () {
    console.log("코멘트 리뷰아이디:", this.reviewId);
    axios({
      method: "GET",
      url: `${SERVER_URL}/reviews/${this.reviewId}/`,
      headers: this.setToken(),
    })
      .then((res) => {
        this.$store.dispatch("createCommentsList", res.date.comment_set);
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