<template>
  <div class="container">
    <input type="text" @change="fetchVideos">
    <button @click="fetchVideos">검색</button>
  </div>
</template>
<script>
import { mapActions } from 'vuex'

export default {
  name: "SearchBar",
  methods: {
    ...mapActions(['fetchVideos']),
    // onInput(e) {
    //   this.$emit('input-change', e.target.value)
    // }
  }
}
</script>
<style scoped>
  input {
    width: 75%;
  }
  div {
    text-align: center;
    margin: 20px;
  }
</style>