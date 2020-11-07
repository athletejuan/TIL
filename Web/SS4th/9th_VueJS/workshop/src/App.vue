<template>
  <div id="app">
    <div id="nav">
      <router-link to="/lunch">Lunch</router-link> |
      <router-link to="/lotto">Lotto</router-link>
    </div>
    <router-view/>
    <h2>App</h2>
    <input v-model="appData" />
    <p>parentData: {{ parentData }}</p>
    <p>childData: {{ childData }}</p>
    <Parent :appData="appData" @parent-input="onParentInput" @child-input="onChildInput" />
  </div>
</template>

<script>
import Parent from './components/Parent.vue'

export default {
  name: 'App',
  data: function () {
    return {
      appData: '',
      parentData: '',
      childData: '',
    }
  },
  methods: {
    onParentInput: function(text) {
      this.parentData = text
    },
    onChildInput: function(text) {
      this.childData = text
    },
  },
  components: {
    Parent,
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

  /* 추가 */
  width: 500px;
  margin: 0 auto;
  border: 1px solid black;
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
