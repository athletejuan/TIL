<template>
  <div>
    <h1>Signup</h1>
    username : <input type="text" v-model="signupInfo.username">
    <br>
    password : <input type="password" v-model="signupInfo.password1">
    <br>
    password2 : <input type="password" v-model="signupInfo.password2">
    <br>
    <button @click="signup">signup</button>
  </div>
</template>
<script>
export default {
  name: 'SignupView',
  data() {
    return {
      signupInfo: {
        username: null,
        password: null,
        password2: null
      }
    }
  },
  methods: {
    signup() {
      this.$emit('onSignup', this.signupInfo)
    }
  },
}
</script>