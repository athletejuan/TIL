<template>
  <ul class="list-group">
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
    videos: {
      type: Array,
      required: true
    }
  },
  methods: {
    onVideoSelect(){
      this.$emit('video-select', this.video)
    }
  }
}
</script>

<style>

</style>