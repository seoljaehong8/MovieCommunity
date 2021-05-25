<template>
  <div v-if="video" class="row my-5">
    <div class="col-12">
      <iframe :src="videoUrl" frameborder="0" width="1080" height="700"></iframe>
    </div>
  </div>
</template>

<script>

export default {
  name: 'MovieVideo',
  props: {
    video: Array,
  },

  computed: {
    videoUrl: function() {
      const videoId = this.video[0].id.videoId
      return `https://www.youtube.com/embed/${videoId}`
    },
  },
}
</script>

<style>

</style>