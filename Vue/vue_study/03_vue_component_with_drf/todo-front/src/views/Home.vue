<template>
  <div class="home">
    <h1>Todo</h1>
    <!-- <img alt="Vue logo" src="../assets/logo.png">
    <HelloWorld msg="Welcome to Your Vue.js App"/> -->
  </div>
</template>

<script>
// @ is an alias to /src
// import HelloWorld from '@/components/HelloWorld.vue'
import router from '../router'

export default {
  name: 'Home',
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
