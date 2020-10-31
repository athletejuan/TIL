<template>
  <ul class="list-group col-lg-4">
    <VideoListItem v-for="video in videos" :key="video.etag" :video="video" @videoSelect="onSelect">
    </VideoListItem>
    {{ videos.length }}
  </ul>
</template>

<script>
import VideoListItem from "./VideoListItem"

export default {
  name: 'VideoList',
  components: {
    VideoListItem,
  },
  props: {
    videos: Array,
  },
  methods: {
    onSelect(video) {
      // console.log(video)
      this.$emit('videoSelect', video)
    }
  }
}
</script>

<style>

</style>