<template>
  <li @click="onVideoSelect" class="list-group-item">
    <img :src="thumbnailURL" class="mr-3" alt="youtube-img">
    {{ video.snippet.title }}
  </li>
</template>

<script>
export default {
  name: "VideoListItem",
  props: {
    video: Object,
  },
  computed: {
    thumbnailURL(){
      return this.video.snippet.thumbnails.default.url
    } 
  },
  methods: {
    onVideoSelect(){
      this.$emit('videoSelect', this.video)
    }
  }
}
</script>

<style scoped>
  .li {
    display: flex;
    cursor: pointer;
  }
  .li:hover {
    background-color: #eee;
  }
</style>