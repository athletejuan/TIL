<template>
  <li class="item" @click="onSelect">
    <img :src="imgSrc" alt="youtube-thumbnail-image">
    {{ video.snippet.title | unescape }}
  </li>
</template>

<script>
import _ from 'lodash'

export default {
  name: 'VideoListItem',
  props: {
    video: {
      type: Object,
    },
  },
  methods: {
    onSelect: function () {
      this.$emit('select-video', this.video)
    }
  },
  computed: {
    imgSrc: function () {
      return this.video.snippet.thumbnails.default.url
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
.item {
  display: flex;        /* 가로배치 및 flex의 CSS 적용을 위함 */
  margin-bottom: 1rem;  /* 아이템들의 상하 여백 */
  cursor: pointer;      /* 마우스를 포인터로 변경 */
}

.item img {
  height: fit-content;   /* 텍스트가 길어져도 이미지는 늘어나지 않게 설정 */
  margin-right: 0.5rem;  /* 이미지와 텍스트 사이의 여백 */
}
</style>