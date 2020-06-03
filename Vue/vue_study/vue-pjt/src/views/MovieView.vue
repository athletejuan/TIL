<template>
  <div class="container">
    <h1 class="mt-5">Movie Collection</h1>
    <button @click="importMovie" v-if="!movies.length" class="btn btn-primary">영화 가져오기</button>
    <MovieList :movies="movies"/>
  </div>
</template>

<script>
// @ is an alias to /src
import axios from 'axios'
import MovieList from '@/components/MovieList.vue'

const MovieUrl = 'https://www.json-generator.com/api/json/get/ceNyuXZmwi?indent=2'

export default {
  name: 'MovieView',
  components: {
    MovieList
  },
  data() {
    return {
      movies: [],
    }
  },
  methods: {
    importMovie() {
      axios.get(MovieUrl)
      .then(res => {
        // console.log(res)
        this.movies = res.data
      })
      .catch(err => console.log(err))
    }
  }
}
</script>
