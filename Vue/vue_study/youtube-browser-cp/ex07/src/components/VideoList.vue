<template>
  <ul class="list-group col-lg-4">
    <VideoListItem v-for="video in videos" :key="video.etag" :video="video" @selected-video="VideoSelect"/>
  </ul>
</template>
<script>
import VideoListItem from './VideoListItem.vue'

export default {
  name: "VideoList",
  components: {
    VideoListItem,
  },
  props: {
    videos: Array,
  },
  methods: {
    VideoSelect(video) {
      this.$emit('selected-video', video)
    }
  }
}
</script>