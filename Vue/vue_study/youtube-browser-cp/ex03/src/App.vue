<template>
  <div>
    <SearchBar @inputChange="onInputChange"></SearchBar>
    <VideoList :videos="videos"></VideoList>
    {{ videos.length }}
  </div>
</template>

<script>
const API_KEY = process.env.VUE_APP_YOUTUBE_API_KEY
const API_URL = 'https://www.googleapis.com/youtube/v3/search'
import axios from 'axios'
import SearchBar from './components/SearchBar'
import VideoList from './components/VideoList'

export default {
  name: 'App',
  data(){
    return{
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
          part: 'snippet',
          type: 'video',
          q: inputValue
        }
      })
      .then((response)=>{
        this.videos = response.data.items
      })
      .catch((err)=>{
        console.log(err)
      })
    }
  }
}
</script>

<style>

</style>