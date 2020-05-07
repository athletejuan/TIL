<template>
  <input @input="onInput" type="text">
</template>

<script>
export default {
  name: "SearchBar",
  methods: {
    onInput: function(e){
      this.$emit('inputChange', e.target.value)
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