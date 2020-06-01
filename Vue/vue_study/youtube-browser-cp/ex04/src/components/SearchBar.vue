<template>
  <div>
    <input @change="onInput" type="text">
  </div>
</template>

<script>
export default {
  name: 'SearchBar',
  methods: {
    onInput(e) {
      if (e.target.value.trim()){
        console.log(e)
        this.$emit('input-change', e.target.value)
      }
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