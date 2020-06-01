<template>
  <div>
    <input @change="onInputChange" type="text">
    <button @click="onInputChange">등록</button>
  </div>
</template>

<script>
export default {
  name: 'SearchBar',
  methods: {
    onInputChange(e) {
      // console.log(e)
      this.$emit('input-change', e.target.value)
    }
  }
}
</script>

<style scoped>
input {
  width: 75%;
}
div{
  text-align: center;
  margin: 20px;
}
</style>