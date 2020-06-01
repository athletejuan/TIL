<template>
  <div>
    <input @change="onInput" type="text">
  </div>
</template>

<script>
export default {
  name: "SearchBar",
  methods: {
    onInput(e){
      // console.log(e.target.value)
      this.$emit('input-change', e.target.value)
    }
  }
}
</script>

<style>

</style>