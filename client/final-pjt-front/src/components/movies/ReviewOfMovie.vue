<template>
  <div v-if="review" class="container">
    <div @click="routeDetailPage(review)" style="cursor: pointer" class="row text-start">
      <div class="offset-1 col-7">
        <div class="row" style="font-size:20px;">
          <div class="col-3 mb-5">
            {{ review.user_name }}
          </div>
          <div class="col-6">
            {{ review.created_at | moment("YYYY-MM-DD HH:mm:ss") }}
          </div>
        </div>
        <div class="row" style="color:white;">
          <h2 style="text-decoration:underline">{{ review.title }}</h2>
          <h5>{{ review.content }}</h5>
        </div>
      </div>
      <div class="col-3">
        <img :src="posterPath" width="150px" alt="" />
      </div>
      <hr style="color:white; margin-top:14px;">
    </div>
  </div>
</template>

<script>
export default {
  name: 'ReviewOfMovie',
  props:{
    review: Object,
  },
  computed: {
    posterPath : function() {
      return `https://image.tmdb.org/t/p/w200${this.review.poster_path}`
    }
  },
  methods: {
    routeDetailPage: function (review) {
      localStorage.setItem(`reviewId`, review.id);
      this.$router.push({ name: "ReviewDetail" });
    },
  },
  created: function() {
    console.log(this.review)
  }
}
</script>

<style>

</style>