<template>
  <ul class="video-list">
    <VideoListItem v-for="video in videos" :key="video.etag" :video="video" @select-video="selectedVideo" />
    <!-- <VideoListItem v-for="(video, idx) in videos" :key="idx" :video="video" @select-video="selectedVideo" /> -->
    <!-- <li v-for="video in videos" :key="video.etag" :video="video" @select-video="selectedVideo">{{ video.snippet.title }}</li> -->
  </ul>
</template>

<script>
import VideoListItem from './VideoListItem'

export default {
  name: 'VideoList',
  components: {
    VideoListItem,
  },
  methods: {
    selectedVideo (video) {
      // console.log(video)
      this.$emit('selected', video)
    }
  },
  props: {
    videos: {
      type: Array,
    }
  }
}
</script>

<style>
.video-list {
  /* ul의 기본 margin,padding,list-style 속성을 초기화 */
  padding: 0;
  margin: 0;
  list-style: none;

	/* Detail,List의 7:3 가로비율에서 3만큼의 길이를 지정 */
  width: 30%;
}
</style>