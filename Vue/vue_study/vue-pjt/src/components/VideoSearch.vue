<template>
  <div>
    <input type="text" @change="onInputChange">
    <button @click="onInputChange">검색</button>
  </div>
</template>

<script>
export default {
  name: 'VideoSearch',
  methods: {
    onInputChange(e) {
      if (e.target.value.trim()) {
        this.$emit('input-change', e.target.value + ' trailer')
      }
      e.target.value = ''
    }
  }
}
</script>

<style>

</style>