<template>
  <div class="container">
    <input type="text" @change="onInput">
    <button @click="onInput">검색</button>
  </div>
</template>
<script>
export default {
  name: "SearchBar",
  methods: {
    onInput(e) {
      this.$emit('input-change', e.target.value)
    }
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