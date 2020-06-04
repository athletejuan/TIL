<template>
  <div class="home">
    <h1>Todo</h1>
  </div>
</template>

<script>
import router from '../router'
export default {
  name: 'home',
  components: {

  },
  mounted() {
    this.checkLoggedIn()
  },
  methods: {
    checkLoggedIn() {
      this.$session.start()
      if (!this.$session.has("jwt")){
        router.push("/login")
      }
    }
  }
}
</script>

<style>

</style>