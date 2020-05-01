<template>
  <li class="list-group-item">
    <!-- VideoListItem -->
    <img :src="thumbnailUrl" class="mr-3" alt="youtube-image">
    <div class="media-body">
      {{ video.snippet.title }}
    </div>
  </li>
</template>

<script>
export default {
  name: 'VideoListItem',
  props: {
    video: Object, // Validation
  },
  computed: {
    thumbnailUrl() {
      return this.video.snippet.thumbnails.default.url;
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