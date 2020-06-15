<template>
  <li class="list-group-item" @click="VideoSelect">
    <img :src="thumbnailUrl" class="mr-3" alt="youtube-thumbnail-img">
    <div class="media-body" v-html="video.snippet.title">{{ video.snippet.title }}</div>
  </li>
</template>
<script>
export default {
  name: "VideoListItem",
  props: {
    video: Object,
  },
  methods: {
    VideoSelect() {
      // this.$emit('selected-video', this.video)
      this.$store.commit('setSelectedVideo', this.video)
    }
  },
  computed: {
    thumbnailUrl() {
      return this.video.snippet.thumbnails.default.url
    }
  }
}
</script>
<style scoped>
li {
  display: flex;
  cursor: pointer;
}
li:hover {
  background-color: #eee;
}
</style>