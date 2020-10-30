<template>
  <div id="app">
    <SearchBar @inputChange="onInputChange"></SearchBar>
    <VideoList :videos="videos"></VideoList>
  </div>
</template>

<script>
const API_KEY = process.env.VUE_APP_YOUTUBE_API_KEY
const API_URL = 'https://www.googleapis.com/youtube/v3/search'
import axios from 'axios'
import SearchBar from './components/SearchBar';
import VideoList from './components/VideoList'

export default {
  name: 'App',
  data () {
    return {
      videos: [],
    }
  },
  components: {
    SearchBar,
    VideoList,
  },
  methods: {
    onInputChange (inputValue) {
      axios.get(API_URL, {
        params: {
          key: API_KEY,
          type: 'video',
          part: 'snippet',
          q: inputValue
        }
      })
      .then((response) => {
        this.videos = response.data.items
      })
      .catch((err) => {
        console.log(err)
      })
    }
  }
}
</script>

<style>

</style>
