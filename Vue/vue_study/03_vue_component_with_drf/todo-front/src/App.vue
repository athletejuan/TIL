<template>
  <div id="app">
    <div id="nav">
      <div class="logout-user" v-if="isAuthenticated">
        <router-link to="/">Home</router-link> |
        <router-link @click.native="logout" to="/logout">Logout</router-link>
      </div>
      <div class="login-user" v-else>
        <router-link to="/login">Login</router-link>
      </div>
    </div>
    <div class="container col-6">
      <router-view/>
    </div>
  </div>
</template>

<script>
export default {
  name: 'App',
  data: function(){
    return {
			// 세션이 존재하는지 여부 확인
      isAuthenticated: this.$session.exists()
    }
  },
  updated: function() {
		// 세션이 존재하는지 여부 확인
    this.isAuthenticated = this.$session.exists()
  },
  methods: {
    logout: function() {
      // 세션을 삭제 후 로그인 페이지로 이동
      this.$session.destroy()
      this.$router.push('/login')
    }
  }
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
