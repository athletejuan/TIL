<template>
  <div id="app">
    <header>
      <h1><span class="green">Vue</span>-<span class="red">Tube</span></h1>
      <SearchBar @search="onSearch"></SearchBar>
    </header>
    <section>
      <VideoDetail :selectedVideo="selectedVideo" />
      <VideoList :videos="videos" @selected="videoSelect"></VideoList>
    </section>
  </div>
</template>

<script>
const API_KEY = process.env.VUE_APP_VUETUBE_API_KEY
const API_URI = 'https://www.googleapis.com/youtube/v3/search'
import axios from 'axios'
import SearchBar from './components/SearchBar'
import VideoList from './components/VideoList'
import VideoDetail from './components/VideoDetail'

export default {
  name: 'App',
  data: function () {
    return {
      videos: [],
      selectedVideo: null,
      // selectedVideo: '',
    }
  },
  components: {
    SearchBar,
    VideoList,
    VideoDetail,
  },
  methods: {
    onSearch(query) {
      axios.get(API_URI, {
        params: {
          key: API_KEY,
          part: 'snippet',
          type: 'video',
          q: query
        }
      })
      .then(res => {
        // console.log(res.data)
        this.videos = res.data.items
        if (!this.selectedVideo) {
          this.selectedVideo = this.videos[0]
        }
      })
      .catch(err => {
        console.error(err)
      })
    },
    videoSelect(video) {
      // console.log(video)
      this.selectedVideo = video
    }
  }
}
</script>

<style>
h1 {
  text-align: center;
}
.green {
  color: green;
}
.red {
  color: red;
}
section, header {
  width: 80%;       /* 전체 너비의 80프로 */
  margin: 0 auto;   /* 양 옆 마진을 균등히 */
  padding: 1rem 0;  /* 위,아래 패딩 */
}

section {
  display: flex;  /* Detail,List를 가로 배치 */
}
</style>
