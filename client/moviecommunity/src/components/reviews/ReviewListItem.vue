<template>
  <div class="container" >
    <div class="row border-change" style="cursor: pointer;" @click="routeDetailPage(review)">
      <div class="offset-2 col-3">       
        <p class="movie-title">{{ review.movie_title }}</p>
        <br>
        <a class="content-summury review-title">{{review.title}}</a>       
        <p class="content-summury review-content animate__animated animate__fadeInLeft">{{review.content}}</p>
        <!-- <p>작성시간 : {{ review.created_at | moment('YYYY-MM-DD HH:mm:ss') }}</p> -->
        <p class="writer">작성자 : {{ review.user_name }}</p>        
        <p class="date">{{ review.updated_at | moment('YYYY-MM-DD HH:mm:ss') }}</p>
      </div>

      <div class="col-5">
        <img :src="getMoviePosterPath" alt="" />
      </div>

      <hr />
    </div>
  </div>
</template>

<script>
// import axios from "axios"
import Vue from "vue";
import vueMoment from "vue-moment";
Vue.use(vueMoment);

// const SERVER_URL = process.env.VUE_APP_SERVER_URL

export default {
  name: "ReviewListItem",

  props: {
    review: Object,
  },
  computed: {
    getMoviePosterPath() {
      return `https://image.tmdb.org/t/p/w200${this.review.poster_path}`;
    },
  },
  methods: {
    routeDetailPage: function (review) {
      localStorage.setItem(`reviewId`, review.id);
      this.$router.push({ name: "ReviewDetail" });
    },
  },
};
</script>

<style>
.movie-title {
  font-size: x-large;
  text-align: left;
}

.content-summury {
  overflow: hidden;
  text-overflow: ellipsis;
  white-space: nowrap;
}

.review-title {
  font-size: x-large;
  text-decoration: underline;
}

.review-content {
  color: black;
  /* animation:  bounce;
  animation-duration: 2s;
  --animate-repeat: 2; */
}

.writer {
  /* display: inline-block; */
  text-align: right;
}

.date {
  /* display: inline-block; */
  text-align: right;
}

.border-change {
    border-radius: 30px;
    background-color: #F6F6F6;
    margin: 0 auto;
}

</style>