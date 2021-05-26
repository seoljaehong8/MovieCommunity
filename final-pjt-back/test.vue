<template>
  <div>
    <h1 style="color:white; margin-bottom:80px;">My Profile</h1>
    <div class="container">
      <div class="row">
        <div class="offset-3 col-3">
          <span class="profile-picture">
            <i class="fas fa-user"> </i>
            </span>
        </div>
        <div class="col-3">
          <div class="row">
            <h1 style="color:white; margin-bottom:100px;">{{userName}}</h1>
          </div>
          <div class="row profile-count">
            <div class="col">리뷰</div>
            <div class="col">평점</div>
            <div class="col">찜</div>
          </div>
          <div class="row profile-count" v-if="myProfile">
            <div class="col">{{myProfile.review_count}}</div>
            <div class="col">{{myProfile.rating_count}}</div>
            <div class="col">{{myProfile.like_movies_count}}</div>
          </div>
        </div>
      </div>
      <div class="row mb-5">
        <div id="review" @click="clickReview" class="offset-1 col-2 align-self-center category" :class="{'category-background':isReview}">내 리뷰</div>
        <div id="rating" @click="clickRating" class="col-2 align-self-center category" :class="{'category-background':isRating}">평점준 영화</div>
        <div id="like" @click="clickLike" class="col-2 align-self-center category" :class="{'category-background':isLike}">찜한 영화</div>
      </div>
      <div class="row" v-if="isReview">
        <ReviewListItem v-for="(review, idx) in reviews"
        :key="idx"
        :review="review"
        />
      </div>
      <div class="cla" v-if="isRating">

      </div>
    </div>
    
  </div>
</template>

<script>
import jwt_decode from 'jwt-decode'
import axios from 'axios'
import ReviewListItem from '@/components/reviews/ReviewListItem.vue'

const SERVER_URL = process.env.VUE_APP_SERVER_URL;


const token = localStorage.getItem('jwt')
let userId = ''
let decoded = null
let username = null
if (token) {
  const decoded = jwt_decode(token)
  console.log(decoded)
  userId = decoded.user_id
  username = decoded.username
}

export default {
  name: 'Profile',
  components: {
    ReviewListItem,
  },
  data: function() {
    return {
      likeMovies: null,
      reviews: null,
      myProfile: null,
      isLike: true,
      isRating: false,
      isReview: false,
      myRatingMovies: [],
    }
  },
  computed: {
    userName: function() {
      return username
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
    clickReview: function() {
      console.log('click review')
      this.isReview = true
      this.isRating = false
      this.isLike = false
      const info = document.querySelector('#review')
      info.classList.add('category-background')
      console.log(this.isReview,this.isRating)
    },
    clickRating: function() {
      console.log('click rating')
      this.isRating = true
      this.isReview = false
      this.isLike = false
      const info = document.querySelector('#rating')
      info.classList.add('category-background')
      console.log(this.isReview,this.isRating)
    },
    clickLike: function() {
      console.log('click like')
      this.isLike = true
      this.isRating = false
      this.isReview = false
      const like = document.querySelector('#like')
      like.classList.add('category-background')
    },
    getMyReviews: function() {
      const reviews = this.$store.getters.getReviewList
      const myReviews = reviews.filter(review=> {
        return review.user_name === this.userName
      })
      return myReviews
    },
  },
  created: function() {
    axios({
        method: 'GET',
        url: `${SERVER_URL}/accounts/${userId}/`,
        headers: this.setToken()
      })
      .then(res => {
        this.myProfile = res.data
        this.reviews = res.data.review_set
        console.log(res.data)
        this.likeMovies = res.data.like_movies
      })
      .catch(err => {
        console.log(err)
      })
    
  }
  

}
</script>

<style scoped>
.profile-picture{
  font-size: 200px;
  color: white;
}
.profile-count{
  color: white;
  font-size:30px;
}
.category {
  font-size: 30px;
  color: white;
  font-weight:400;
  border-radius: 12px;
  cursor: pointer;
}
.category:hover{
  background-color: gray;
}
.category-background {
  color: black;
  background-color:lightgray;
}
</style>