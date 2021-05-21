<template>
  <div>
    <h1>detail</h1>

    {{ review }}
  </div>

</template>

<script>


export default {
  name: 'ReviewListDetail',
  props: {
    review: Object,
  },
  created: function() {
    console.log(this.review)
  }
}
</script>

<style>

</style>