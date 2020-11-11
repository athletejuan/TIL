<template>
  <div class="video-detail" v-if="selectedVideo">
    <div class="video-container">
      <iframe :src="videoSrc" frameborder="0"></iframe>
    </div>
    <h4>{{ selectedVideo.snippet.title | unescape }}</h4>
    <hr>
    <p>{{ selectedVideo.snippet.discription | unescape }}</p>
  </div>
</template>

<script>
import _ from 'lodash'

export default {
  name: 'VideoDetail',
  props: {
    selectedVideo: {
      type: Object,
      // type: [Object, String],
    }
  },
  computed: {
    videoSrc () {
      const videoId = this.selectedVideo.id.videoId
      return `http://www.youtube.com/embed/${videoId}`
    }
  },
  filters: {
    unescape: function (text) {
      return _.unescape(text)
    }
  }
}
</script>

<style>
.video-detail {
  width: 70%;           /* Detail,List를 전체 가로비율을 7:3 으로 */
  padding-right: 1rem;  /* Detail과 List 사이의 여백 */
}

.video-container {
  position: relative;   /* iframe을 container를 기준으로 위치를 지정 위함 */
  padding-top: 56.25%;  /* 유튜브 비디오 비율을 맞추기 위한 높이 설정 */
}

.video-container > iframe {
  position: absolute;   /* container를 기준으로 위치를 지정*/
  top: 0;               /* container의 가장 위쪽으로 위치를 지정 */
  width: 100%;
  height: 100%;
}
</style>