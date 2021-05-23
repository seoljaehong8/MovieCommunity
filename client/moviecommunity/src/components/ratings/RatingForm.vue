<template>
  <div>
    <button type="button" class="btn btn-primary" data-bs-toggle="modal" data-bs-target="#exampleModal">
      평점등록
    </button>

    <div class="modal fade" id="exampleModal" tabindex="-1" aria-labelledby="exampleModalLabel" aria-hidden="true">
      <div class="modal-dialog">
        <div class="modal-content">
          <div class="modal-header">
            <h5 class="modal-title" id="exampleModalLabel">영화선택</h5>
            <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
          </div>
          <div class="modal-body">

            <div              
              style="
                background: white;
                overflow: auto;
                padding: 10px;
                padding-bottom: 20px;
                display:inline-block;
              "
            >
              <star-rating        
                :show-rating="false"
                :animate="true"
                :star-size="50"
                :rounded-corners="true"
                :border-width="7"
                :increment="0.5"
                :glow="10" glow-color="#ffd055"                      
                v-model="rating"
              ></star-rating>
              <h2 class="mt-3">{{currentRatingText}}</h2>

            </div>

            <div>
              <input v-model="content" type="text" placeholder="이 영화에 대한 소감을 적어주세요.">
            </div>
            
          </div>
          <div class="modal-footer">
            <button type="button" @click="createRating" class="btn btn-secondary" data-bs-dismiss="modal">등록</button>
          </div>
        </div>
      </div>
    </div>


  </div>
</template>

<script>
import StarRating from "vue-star-rating";
import axios from 'axios'

const SERVER_URL = process.env.VUE_APP_SERVER_URL

export default {
  name: 'RatingForm',
  components: {
    StarRating,
  },
  props: {
    movie: Object
  },
  data() {
    return {
      content: null,
      rating: 2.5,
      resetableRating: 2,
      currentRating: "No Rating",
      mouseOverRating: null,
    };
  },
  computed: {
    currentRatingText() {
      return this.rating
        ? this.rating*2 + " 점을 선택하셨습니다."
        : "No rating selected";
    },
    mouseOverRatingText() {
      return this.mouseOverRating
        ? "Click to select " + this.mouseOverRating + " stars"
        : "No Rating";
    },
  },
  methods: {
    showCurrentRating(rating) {
      this.currentSelectedRating =
        rating === 0
          ? this.currentSelectedRating
          : "Click to select " + rating + " stars";
    },
    setCurrentSelectedRating(rating) {
      this.currentSelectedRating = "You have Selected: " + rating + " stars";
    },
    setToken: function () {
      const token = localStorage.getItem('jwt')
      const config = {
        Authorization: `JWT ${token}`
      }
      return config
    },
    createRating: function() {
      const data = {
        movie_id : this.movie.id,
        grade : this.rating*20,
        content : this.content
      }
      axios({
        method : 'POST',
        url : `${SERVER_URL}/movies/rating/${this.movie.id}/`,
        headers : this.setToken(),
        data: data
      })
        .then(res=>{
          console.log(res)
        })
        .catch(err=>{
          console.log(err)
        })
    },
  },
}
</script>

<style>

</style>