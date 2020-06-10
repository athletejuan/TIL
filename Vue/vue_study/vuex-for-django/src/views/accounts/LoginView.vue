<template>
  <div>
    <h1>login</h1>
    username : <input type="text" v-model="loginInfo.username"><br>
    password : <input type="password" v-model="loginInfo.password"><br>
    <button @click="login(loginData)">login</button>
  </div>
</template>

<script>
import { mapActions } from 'vuex'

export default {
  name: 'LoginView',
  data() {
    return {
      loginInfo: {
        username: null,
        password: null,
      }
    }
  },
  methods: {
    ...mapActions(['login'])
    // login() {
    //   this.$emit('onLogin', this.loginInfo)
    // }
  },
}
</script>

<style>

</style>