<template>
  <div class="container">
    <!-- step.3 -->
    <!--  1. App 이 'inputChange' 라는 시그널(이벤트)를 기다리고 있는 상황. -->
    <!--  2. 만약 inputChange 가 일어나면 => onInputChange 라는 methods 가 실행됨 -->
    <SearchBar @inputChange="onInputChange"></SearchBar>
    <div class="row">
      <!-- bind 까지는 했으나 어떤 data를 내려보내야 할 것인가..? -->
      <VideoDetail :video="selectedVideo"></VideoDetail>
      <!-- key videos(우리가 지정) - value 'videos'(data 의 이름) -->
      <VideoList @videoSelect="onVideoSelect" :videos="videos"></VideoList>
      <!-- {{ videos.length }} -->
    </div>
  </div>
</template>

<script>
// step.1
import axios from 'axios'
import SearchBar from './components/SearchBar'
import VideoList from './components/VidoeList'
import VideoDetail from './components/VideoDetail'
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
  // step.2
  components: {
    SearchBar,
    VideoList,
    VideoDetail,
  },
  methods: {
    onVideoSelect(video){
      this.selectedVideo = video;
      // console.log(video)
    },
    // 3. onInputChange 는 여기에 정의되어 있음 
    // inputValue 는 .$emit() 의 두번째 인자가 자동으로 넘어온 것이다. Vue 의 콜백구성.
    onInputChange(inputValue){
      axios.get(API_URL, {
        params: {
          key: API_KEY,
          type: 'video',
          part: 'snippet',
          q: inputValue
        }
      })
      .then((response)=>{
        this.videos = response.data.items
        // console.log(response)
      })
      .catch((err)=>{
        console.log(err)
      })
      // console.log(inputValue);
    }
  }
}
</script>

<style>

</style>