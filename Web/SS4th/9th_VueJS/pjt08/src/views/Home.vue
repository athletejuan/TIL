<template>
  <div class="container">
    <div class="card-group">
      <div class="card" style="width: 18rem;">
        <MovieCard :movies="movies"/>
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios'
import MovieCard from '@/components/MovieCard'

const MOVIE_API = process.env.VUE_APP_MOVIE_API_URL
const MOVIE_KEY = process.env.VUE_APP_MOVIE_API_KEY

export default {
  name: 'Home',
  data: function () {
    return {
      movies: [],
    }
  },
  components: {
    MovieCard
  },
  methods: {
    getMovieList: function () {
      axios.get(`${MOVIE_API}/upcoming?api_key=${MOVIE_KEY}`)
        .then((res) => {
          this.movies = res.data.results
        })
        .catch((err) => {
          console.log(err)
        })
    }
  },
  created: function () {
    this.getMovieList()
  },
}
</script>
