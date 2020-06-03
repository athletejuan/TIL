<template>
  <div class="mt-5">
    <div v-if="videos.length">
      <div v-for="video in videos" :key="video.etag">
        <VideoItemDetail :video="video"/>
      </div>
    </div>
  </div>
</template>

<script>
import VideoItemDetail from './VideoItemDetail.vue'
export default {
  name: 'VideoItem',
  components: {
    VideoItemDetail,
  },
  props: {
    videos: Array,
  }
}
</script>

<style>

</style>