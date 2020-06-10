<template>
  <div>
    <h1>Signup</h1>
    username : <input type="text" v-model="signupInfo.username">
    <br>
    password : <input type="password" v-model="signupInfo.password1">
    <br>
    password2 : <input type="password" v-model="signupInfo.password2">
    <br>
    <button @click="signup(signupData)">signup</button>
  </div>
</template>
<script>
import { mapActions } from 'vuex'

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
    ...mapActions('[signup]')
    // signup() {
    //   this.$emit('onSignup', this.signupInfo)
    // }
  },
}
</script>