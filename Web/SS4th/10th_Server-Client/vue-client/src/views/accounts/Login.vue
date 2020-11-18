<template>
  <div>
    <h1>Login</h1>
    <div>
      <label for="username">사용자 이름: </label>
      <input type="text" id="username" v-model="credentials.username">
    </div>
    <div>
      <label for="password">비밀번호: </label>
      <input type="password" id="password" v-model="credentials.password" @keydown.enter="login(credentials)">
    </div>
    <button @click="login(credentials)">로그인</button>
  </div>
</template>

<script>
import axios from 'axios'

const SERVER_URL = 'http://127.0.0.1:8000/accounts'

export default {
  name: 'Login',
  data: function () {
    return {
      credentials: {
        username: '',
        password: '',
      },
    }
  },
  methods: {
    login: function () {
      axios.post(`${SERVER_URL}/api-token-auth/`, this.credentials)
        .then((res) => {
          // console.log(localStorage)
          localStorage.setItem('jwt', res.data.token)
          console.log(localStorage.getItem('jwt'))
          this.$emit('login')
          this.$router.push({ name: 'TodoList' })
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