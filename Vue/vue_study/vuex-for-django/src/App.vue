<template>
  <div class="container col-sm-4">
    <div id="app">
      <div id="nav">
        <router-link to="/">Home</router-link> |
        <span v-if="isLogin">
          <router-link to="/accounts/logout" @click.native="logout">Logout</router-link> |
          <router-link to="/articles/create">Create Article</router-link>
        </span>
        <span v-else>
          <router-link to="/accounts/signup">Signup</router-link> |
          <router-link to="/accounts/login">Login</router-link>
        </span>
      </div>
      <router-view @onLogin="login" @onSignup="signup"/>
    </div>
  </div>
</template>

<script>
import { mapGetters } from 'vuex'
// import axios from 'axios'
// const BACK_URL = 'http://127.0.0.1:8000'

export default {
  name: "App",
  computed: {
    ...mapGetters(['isLoggedIn'])
  },
  // data() {
  //   return {
  //     isLogin: false,
  //   }
  // },
  // mounted() {
  //   if(this.$cookies.isKey('auth-token')){
  //     this.isLogin = true
  //   } else {
  //     this.isLogin = false
  //   }
  //   this.isLoggedIn = this.$cookies.isKey('auth-token')
  // },
  methods: {
    // setCookie(key){
    //   this.$cookies.set('auth-token', key)
    //   this.isLogin = true
    // },
    // signup(info) {
    //   axios.post(`${BACK_URL}/rest-auth/signup/`, info)
    //     .then(res => {
    //       this.setCookie(res.data.key)
    //       this.$router.push('/')
    //     })
    //     .catch(err => {
    //       console.log(err.response.data)
    //     })
    // },
    // login(info) {
    //   axios.post(`${BACK_URL}/rest-auth/login/`, info)
    //     .then(res => {
    //       // console.log(res.data.key)
    //       // this.$cookies.set('auth-token', res.data.key)
    //       this.setCookie(res.data.key)
    //       this.$router.push('/')
    //     })
    //     .catch(err => {
    //       console.log(err.response)
    //       alert(err.response.data.non_field_errors[0])
    //     })
    // },
    // logout(){
    //   const requestHeaders = {
    //     headers: {
    //       Authorization: `Token ${this.$cookies.get('auth-token')}`
    //     }
    //   }
    //   axios.post(`${BACK_URL}/rest-auth/logout/`, null, requestHeaders)
    //     .then(() => {
    //       this.$cookies.remove('auth-token')
    //       this.isLogin = false
    //       this.$router.push('/')
    //     })
    //     .catch(err => { 
    //       console.log(err.response)
    //     })
    // }
  },
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}

#nav {
  padding: 30px;
}

#nav a {
  font-weight: bold;
  color: #2c3e50;
}

#nav a.router-link-exact-active {
  color: #42b983;
}
</style>
