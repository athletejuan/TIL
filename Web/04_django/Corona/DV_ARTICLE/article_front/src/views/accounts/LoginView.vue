<template>
  <div>
    <h1>login</h1>
    username : <input type="text" v-model="loginInfo.username"><br>
    password : <input type="password" v-model="loginInfo.password"><br>
    <button @click="login">login</button>
  </div>
</template>

<script>
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
    login() {
      this.$emit('onLogin', this.loginInfo)
    }
  },
}
</script>

<style>

</style>