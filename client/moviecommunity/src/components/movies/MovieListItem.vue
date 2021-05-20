<template>
  <div class="card col-xl-4 col-12 my-3">
    <img :src="getPosterUrl" class="card-img-top" alt="...">
    <div class="card-body">
      <h5 class="card-title">{{ this.movie.title }}</h5>
      <p class="card-text">{{ this.movie.overview }}</p>
    </div>
  </div>
</template>

<script>
export default {
  name: 'MovieListItem',
  props: {
    movie: Object,
  },
  data: function() {
    return {
      title: [],
    }
  },
  computed: {
    getPosterUrl: function() {
      const url = `https://image.tmdb.org/t/p/w500${this.movie.poster_path}`
      return url
    }
  }
}
</script>

<style>

</style>