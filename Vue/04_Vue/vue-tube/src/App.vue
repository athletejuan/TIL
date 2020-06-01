<template>
  <div id="app">
    <SearchBar @input-change="onInputChange"/>
    <VideoList :videos="videos"/>
    {{ videos.length }}
  </div>
</template>

<script>
import axios from 'axios'
import SearchBar from './components/SearchBar.vue'
import VideoList from './components/VideoList.vue'

const API_KEY = process.env.VUE_APP_YOUTUBE_API_KEY
const API_URL = 'https://www.googleapis.com/youtube/v3/search'

export default {
  name: 'App',
  data() {
    return {
      videos: [],
    }
  },
  components: {
    SearchBar,
    VideoList,
  },
  methods: {
    onInputChange(inputValue){
      axios.get(API_URL, {
        params: {
          key: API_KEY,
          type: 'video',
          part: 'snippet',
          q: inputValue
        }
      })
      .then(res => {
        this.videos = res.data.items
      })
      .catch(err => {
        console.log(err)
      })
    }
  }
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
