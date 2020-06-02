<template>
  <div class="container">
    <SearchBar @input-change="onInputChange"/>
    <div class="row">
      <VideoDetail :video="selectedVideo"/>
      <VideoList @video-select="onVideoSelect" :videos="videos"/>
    </div>
  </div>
</template>

<script>
import axios from 'axios'
import SearchBar from './components/SearchBar.vue'
import VideoList from './components/VideoList.vue'
import VideoDetail from './components/VideoDetail.vue'

const API_KEY = process.env.VUE_APP_YOUTUBE_API_KEY
const API_URL = 'https://www.googleapis.com/youtube/v3/search'

export default {
  name: 'App',
  data() {
    return {
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
    onVideoSelect(video){
      // console.log(video)
      this.selectedVideo = video
    },
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
        // console.log(res)
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

</style>
