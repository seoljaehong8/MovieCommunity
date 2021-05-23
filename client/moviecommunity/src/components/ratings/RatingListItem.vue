<template>
  <div>
    <div class="star-ratings">
      <div 
        class="star-ratings-fill space-x-2 text-lg"
        :style="{ width: ratingToPercent() + '%' }"
      >
        <span>★</span><span>★</span><span>★</span><span>★</span><span>★</span>
      </div>
      <div class="star-ratings-base space-x-2 text-lg">
        <span>★</span><span>★</span><span>★</span><span>★</span><span>★</span>
      </div>
    </div>
    <h3>별점 : {{rating.grade}}</h3>
    <h3>작성자 : {{rating.user_name}}</h3>
    <h3>내용 : {{rating.content}}</h3>
    <button @click="deleteRating">삭제</button>
    <hr>
  </div>
</template>

<script>
import axios from 'axios'

const SERVER_URL = process.env.VUE_APP_SERVER_URL

export default {
  name: 'RatingListItem',
  props:{
    rating: Object,
  },

  methods: {
    ratingToPercent: function() {
      const score = this.rating.grade
      return score;
    },
    setToken: function () {
      const token = localStorage.getItem('jwt')
      const config = {
        Authorization: `JWT ${token}`
      }
      return config
    },
    deleteRating: function() {
      axios({
        method: 'DELETE',
        url : `${SERVER_URL}/movies/rating/${this.rating.id}/`,
        headers : this.setToken(),
      })
        .then(res => {
          console.log(res)
          alert('삭제되었습니다.')
        })
        .catch(err=>{
          console.log(err)
        })
    }
  },
}
</script>

<style>

.star-ratings {
  color: #aaa9a9; 
  position: relative;
  unicode-bidi: bidi-override;
  width: max-content;
  -webkit-text-fill-color: transparent; /* Will override color (regardless of order) */
  -webkit-text-stroke-width: 1.3px;
  -webkit-text-stroke-color: #2b2a29;
}
 
.star-ratings-fill {
  font-size: 30px;
  color: #fff58c;
  padding: 0;
  position: absolute;
  z-index: 1;
  display: flex;
  top: 0;
  left: 0;
  overflow: hidden;
  -webkit-text-fill-color: gold;
}
 
.star-ratings-base {
  font-size: 30px;
  z-index: 0;
  padding: 0;
}

</style>