<template>
  <div id="app">
    <div>
      <button @click="statusIndex">Index</button>
      <button @click="statusLunch">Lunch</button>
      <button @click="statusLotto">Lotto</button>
      <button @click="welcoming">Welcome</button>
    </div>
    <div>
      <input v-model="welcomeMessage"/>
      <Welcome v-if="status === 'welcome'" @welcome="sayHi" :welcomeMessage="welcomeMessage"/>
    </div>
    <!-- step.3 사용한다. -->
    <Index v-if="status === 'index'"/>
    <!-- lunch-menu === lunchMenu === LunchMenu -->
    <!-- lotto === Lotto -->
    <Lunch v-if="status === 'lunch'"/>
    <Lotto v-if="status === 'lotto'"/>
  </div>
</template>

<script>
// 컴포넌트 사용하기
// step.1 : import 한다.
import Index from './components/Index.vue'
import Lunch from './components/Lunch.vue'
import Lotto from './components/Lotto.vue'
import Welcome from './components/Welcome.vue'

export default {
  name: 'App',
  components: {
    // step.2 : 등록한다.
    Index,
    Lunch,
    Lotto,
    Welcome,
  },
  data: function(){
    return {
      status: 'index',
      welcomeMessage: '',
    }
  },
  methods: {
    statusLunch(){
      this.status = 'lunch'
    },
    statusLotto(){
      this.status = 'lotto'
    },
    statusIndex(){
      this.status = 'index'
    },
    welcoming(){
      this.status = 'welcome'
    },
    sayHi(welcomeCount) {
      alert(`you welcomed me ${welcomeCount} times.`)
    },
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
  margin-top: 60px;
}
</style>
