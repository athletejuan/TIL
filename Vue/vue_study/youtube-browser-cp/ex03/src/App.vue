<template>
  <div class="container">
    <SearchBar @inputChange="onInputChange"></SearchBar>
    <VideoDetail :video="selectedVideo"></VideoDetail>
    <VideoList @videoSelect="onVideoSelect" :videos="videos"></VideoList>
    {{ videos.length }}
  </div>
</template>

<script>
const API_KEY = process.env.VUE_APP_YOUTUBE_API_KEY
const API_URL = 'https://www.googleapis.com/youtube/v3/search'
import axios from 'axios'
import SearchBar from './components/SearchBar'
import VideoList from './components/VideoList'
import VideoDetail from './components/VideoDetail'

export default {
  name: 'App',
  data(){
    return{
      videos: [],
      selectedVideo: null,
    }
  },
  components: {
    SearchBar,
    VideoList,
    VideoDetail,
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
    },
    onVideoSelect(video){
      this.selectedVideo = video;
    }
  }
}
</script>

<style>

</style>