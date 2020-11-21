<template>
  <!-- 배경이미지 추가 -->
  <div id="app" :style="{ backgroundImage: `url(${backgroundUrl})`}">
    <div id="nav">
      <router-link to="/">Home</router-link> |
      <router-link to="/Random">Random</router-link> |
      <router-link to="/MyMovieList">MyMovieList</router-link>
    </div>
    <router-view/>
  </div>
</template>

<script>
// 배경이미지 추가
import backgroundUrl from "@/assets/images/ss4th.png";

export default {
  data() {
    return {
      backgroundUrl,
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
