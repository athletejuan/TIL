<template>
  <div class="container">
    <h1 class="mt-5">영화 예고편 검색</h1>
    <VideoSearch @input-change="searchVideo"/>
    <VideoItem :videos="videos"/>
  </div>
</template>

<script>
import axios from 'axios'
import VideoSearch from '@/components/VideoSearch.vue'
import VideoItem from '@/components/VideoItem.vue'

const API_KEY = process.env.VUE_APP_YOUTUBE_API_KEY
const API_URL = 'https://www.googleapis.com/youtube/v3/search'

export default {
  name: 'VideoView',
  components: {
    VideoSearch,
    VideoItem,
  },
  data() {
    return {
      videos: [],
    }
  },
  methods: {
    searchVideo(inputValue) {
      axios.get(API_URL, {
        params: {
          key: API_KEY,
          part: 'snippet',
          q: inputValue
        }
      })
      .then(res => {
        // console.log(res)
        this.videos = res.data.items
      })
      .catch(err => console.log(err))
    }
  }
}
</script>

<style>

</style>