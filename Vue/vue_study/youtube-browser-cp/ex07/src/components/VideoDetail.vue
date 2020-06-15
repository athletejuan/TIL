<template>
  <div v-if="$store.state.selectedVideo" class="col-lg-8">
    <div class="embed-responsive embed-responsive-16by9">
      <iframe :src="$store.getters.videoUrl" frameborder="0" class="embed-responsive-item"></iframe>
    </div>
    <div class="details">
      <h4 v-html="$store.getters.videoTitle"></h4>
      <p>{{ $store.getters.videoDescription }}</p>
    </div>
  </div>
</template>

<script>
import { mapGetters } from 'vuex'

export default {
  name: "VideoDetail",
  props: {
    video: Object,
  },
  computed: {
    ...mapGetters(['videoUrl', 'videoTitle', 'videoDescription'])
    // videoUrl() {
    //   const videoId = this.video.id.videoId
    //   return `https://www.youtube.com/embed/${videoId}`
    // }
  }
}
</script>
<style scoped>
  .details {
    margin-top: 10px;
    padding: 10px;
    border: 1px solid #ddd;
    border-radius: 4px;
  }
</style>