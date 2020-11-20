<template>
  <div>
    <button @click="randomMovie">Pick</button>
    <h4>{{ title }}</h4>
  </div>
</template>

<script>
import _ from 'lodash'
import axios from 'axios'

const MOVIE_API = process.env.VUE_APP_MOVIE_API_URL
const MOVIE_KEY = process.env.VUE_APP_MOVIE_API_KEY

export default {
  name: 'Random',
  data: function () {
    return {
      title: '',
    }
  },
  methods: {
    randomMovie: function () {
      axios.get(`${MOVIE_API}/upcoming?api_key=${MOVIE_KEY}`)
        .then((res) => {
          const randomIdx = _.random(res.data.results.length - 1)
          const movie_list = res.data.results
          this.title = movie_list[randomIdx].title
        })
        .catch((err) => {
          console.log(err)
        })
    }
  }
}
</script>
