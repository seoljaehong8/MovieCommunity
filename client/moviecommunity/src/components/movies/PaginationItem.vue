<template>
  <li class="page-item"><a class="page-link" href="#">{{ this.pageNumber }}</a></li>
</template>

<script>
export default {
  name: 'PaginationItem',
  props: {
    pageNumber: Number,
  },
  
}
</script>

<style>

</style>