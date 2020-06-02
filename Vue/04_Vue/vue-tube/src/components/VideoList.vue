<template>
  <ul class="col-lg-4 list-group">
    <VideoListItem v-for="video in videos" :key="video.etag" :video="video" @video-select="onVideoSelect"/>
  </ul>
</template>

<script>
import VideoListItem from './VideoListItem.vue'

export default {
  name: 'VideoList',
  components: {
    VideoListItem,
  },
  props: {
    videos: Array,
  },
  methods: {
    onVideoSelect(video){
      this.$emit('video-select', video)
    }
  }
}
</script>

<style>

</style>