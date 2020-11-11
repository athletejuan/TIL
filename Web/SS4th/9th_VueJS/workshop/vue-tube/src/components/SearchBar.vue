<template>
  <div class="search-bar">
    <input @keydown.enter="onInput" type="text" placeholder="Youtube Search" >
  </div>
</template>

<script>
export default {
  name: "SearchBar",
  methods: {
    onInput: function () {
      this.$emit('search', event.target.value)
      event.target.value = ''
    }
  }
}
</script>

<style>
.search-bar > input {
  width: 100%;      /* 가로 크기를 끝까지 */
  padding: 0.5rem;  /* input 안쪽의 여백을 여유롭게 */
  font-size: 1rem;
}

.search-bar {
  transition: margin 0.5s;
}
</style>