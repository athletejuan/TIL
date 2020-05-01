<template>
  <ul class="list-group">
    <VideoListItem v-for="video in videos" :key="video.etag" :video="video">

    </VideoListItem>
    <!-- VideoList
    {{ videos.length }} -->
  </ul>
</template>

<script>
import VideoListItem from "./VideoListItem";

export default {
  name: 'VideoList',
  components: {
    VideoListItem,
  },
  // props의 value가 배열인 이유? 여러개 넘어올 수 있음
  // + 유효성 검사를 하려면 Object.
  props: {
    videos: Array, // videos가 Array 인지 먼저 확인
  },
};
</script>

<style>

</style>