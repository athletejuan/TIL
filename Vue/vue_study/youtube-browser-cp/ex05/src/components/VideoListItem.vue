<template>
  <li class="list-group-item" @click="onVideoSelected" >
    <img :src="thumbnailUrl" alt="youtube-thumbnail-image">
    <div class="media-body">
      {{ video.snippet.title }}
      <!-- <p>{{ video.description }}</p> -->
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
    onVideoSelected(){
      console.log(this.video)
      this.$emit('video-select', this.video)
    }
  },
  computed: {
    thumbnailUrl() {
      return this.video.snippet.thumbnails.default.url
    }
  },
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
.media-body {
  margin: auto 0;
}
</style>