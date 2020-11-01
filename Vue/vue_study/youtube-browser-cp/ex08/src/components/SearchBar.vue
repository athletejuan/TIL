<template>
  <div>
    <input @keyup.enter="onInput" type="text">
    <button @click="onInput">검색</button>
  </div>
</template>

<script>
export default {
  name: 'SearchBar',
  methods: {
    onInput(e) {
      this.$emit('inputChange', e.target.value);
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