<template>
  <div class="col-3 my-2">
    <div class="card" style="width: 15rem;">
      <img :src="movie.poster_url" class="card-img-top" alt="...">
      <div class="card-body">
        <h5 class="card-title">{{ movie.title }}</h5>
        <a data-toggle="modal" :data-target="'#movie-'+movie.id" class="btn btn-primary text-light">영화 상세보기</a>
      </div>
    </div>
    <MovieListItemModal :movie="movie"/>
  </div>
</template>

<script>
import MovieListItemModal from './MovieListItemModal.vue'

export default {
  name: 'MovieListItem',
  components: {
    MovieListItemModal
  },
  props: {
    movie: Object
  }
}
</script>

<style>

</style>