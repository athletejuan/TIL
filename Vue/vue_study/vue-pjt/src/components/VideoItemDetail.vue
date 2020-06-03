<template>
  <div class="mt-3">
    <h4 v-html="video.snippet.title"></h4>
    <div class="embed-responsive embed-responsive-16by9 w-75 mx-auto">
      <iframe :src="VideoUrl" frameborder="0"></iframe>
    </div>
  </div>
</template>

<script>
export default {
  name: 'VideoItemDetail',
  props: {
    video: Object
  },
  computed: {
    VideoUrl(video) {
      console.log(video)
      const videoId = this.video.id.videoId
      return `https://www.youtube.com/embed/${videoId}`
    }
  }
}
</script>

<style>

</style>