<template>
  <div v-if="review" class="container">
    <div @click="routeDetailPage(review)" style="cursor: pointer" class="row">
      <div class="offset-2 col-3">
        <img :src="posterPath" width="150px" alt="" />
      </div>
      <div class="col-5">
        <h2>작성자 : {{ review.user_name }}</h2>
        <h2>
          작성시간 : {{ review.created_at | moment("YYYY-MM-DD HH:mm:ss") }}
        </h2>
        <h2>
          수정시간 : {{ review.updated_at | moment("YYYY-MM-DD HH:mm:ss") }}
        </h2>
        <h2>글 제목 : {{ review.title }}</h2>
        <h2>내용 : {{ review.content }}</h2>
      </div>
      <hr>
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