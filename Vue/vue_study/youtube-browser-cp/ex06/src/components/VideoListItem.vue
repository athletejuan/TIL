<template>
  <li class="list-group-item" @click="selectedVideo">
    <img :src="thumbnailUrl" alt="youtube-thumbnail-image">
    <div>
      {{ video.snippet.title }}
    </div>
  </li>
</template>

<script>
export default {
  name: 'VideoListItem',
  props: {
    video: Object,
  },
  methods: {
    selectedVideo() {
      this.$emit('select-video', this.video)
    }
  },
  computed: {
    thumbnailUrl() {
      return this.video.snippet.thumbnails.default.url
    }
  }
}
</script>

<style>
li {
  display: flex;
  cursor: pointer;
}
li:hover {
  background-color: #eee;
}
</style>