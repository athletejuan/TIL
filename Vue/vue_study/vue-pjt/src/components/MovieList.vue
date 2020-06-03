<template>
  <div class="row mt-5">
    <MovieListItem v-for="movie in movies" :key="movie.id" :movie="movie"/>
  </div>
</template>

<script>
import MovieListItem from './MovieListItem.vue'

export default {
  name: 'MovieList',
  props: {
    movies: Array,
  },
  components: {
    MovieListItem
  }
}
</script>

<style>

</style>