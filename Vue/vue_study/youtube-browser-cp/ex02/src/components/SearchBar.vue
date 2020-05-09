<template>
  <div>
    <!-- enter 누를때만 검색 -->
    <input @keyup.enter="onInput" type="text">
  </div>
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