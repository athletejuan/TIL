<template>
  <ul class="list-group">
    <VideoListItem v-for="video in videos" :key="video.etag" :video="video" @select-video="selectedVideo"/>
  </ul>
</template>

<script>
import VideoListItem from './VideoListItem.vue'

export default {
  name: 'VideoList',
  components: {
    VideoListItem
  },
  props: {
    videos: Array,
  },
  methods: {
    selectedVideo(video){
      this.$emit('video-select', video)
    }
  }
}
</script>

<style>

</style>