<template>
  <li @click="onVideoSelect" class="list-group-item">
    <img :src="thumbnailUrl" alt="youtube-thumbnail-image">
    <div class="media-body">
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
  computed: {
    thumbnailUrl(){
      return this.video.snippet.thumbnails.default.url;
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
  li {
    display: flex;
    cursor: pointer;
  }
  li:hover{
    background-color: #eee;
  }
</style>