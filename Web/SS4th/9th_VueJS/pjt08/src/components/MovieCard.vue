<template>
  <div class="row row-cols-4">
    <div class="px-2" v-for="(movie, idx) in movies" :key="idx" >
      <img :src="`https://image.tmdb.org/t/p/w300${movie.poster_path}`" class="card-img-top" alt="movie_poster">
      <div class="card-body">
        <h5 class="card-title">{{ movie.title }}</h5>
        <p class="card-text">{{ movie.overview }}</p>
        <a href="#" class="btn btn-primary">Go somewhere</a>
      </div>
    </div>
  </div>
</template>

<script>
// const movie_poster = 'https://image.tmdb.org/t/p/w500'

export default {
  name: 'MovieCard',
  props: {
    movies: {
      type: Array,
    }
  }
}
</script>

<style>

</style>