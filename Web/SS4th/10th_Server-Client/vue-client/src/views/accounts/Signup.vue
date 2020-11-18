<template>
  <div>
    <h1>Signup</h1>
    <div>
      <label for="username">사용자 이름: </label>
      <input type="text" id="username" v-model="credentials.username">
    </div>
    <div>
      <label for="password">비밀번호: </label>
      <input type="password" id="password" v-model="credentials.password" @keydown.enter="signup(credentials)">
    </div>
    <div>
      <label for="passwordConfirmation">비밀번호 확인: </label>
      <input type="password" id="passwordConfirmation" v-model="credentials.passwordConfirmation">
    </div>
    <button @click="signup(credentials)">회원가입</button>
  </div>
</template>

<script>
import axios from 'axios'

const SERVER_URL = 'http://127.0.0.1:8000/accounts'

export default {
  name: 'Signup',
  data: function () {
    return {
      credentials: {
        username: '',
        password: '',
        passwordConfirmation: '',
      },
    }
  },
  methods: {
    signup: function () {
      axios.post(`${SERVER_URL}/signup/`, this.credentials)
        .then(() => {
          this.$router.push( { name: 'Login' })
        })
        .catch((err) => {
          console.log(err)
        })
    }
  }
}
</script>

<style>

</style>