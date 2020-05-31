<template>
  <button @click="onWelcome">
    Click me to welcome with {{ welcomeMessage }}
  </button>
</template>

<script>
export default {
  name: 'Welcome',
  data: function() {
    return {
      welcomeCount: 0,
    }
  },
  props: [
    'welcomeMessage',
  ],
  methods: {
    onWelcome: function() {
      this.welcomeCount++
      this.$emit('welcome', this.welcomeCount)
    }
  }
}
</script>

<style>

</style>