<template>
  <div id="app">
    <img alt="Vue logo" src="./assets/logo.png">
    <!-- <HelloWorld msg="Welcome to Your Vue.js App"/> -->
    <TodoInput @sendUserInput="addTodo"/>
    <TodoList :appTodos="todos"/>
  </div>
</template>

<script>
// import HelloWorld from './components/HelloWorld.vue'
import TodoInput from './components/TodoInput.vue'
import TodoList from './components/TodoList.vue'

export default {
  name: 'app',
  data: function(){
    return {
      todos: [],
    }
  },
  components: {
    // HelloWorld
    TodoInput,
    TodoList,
  },
  methods: {
    addTodo: function(userInput){
      console.log("이벤트 받음")
      this.todos.push(userInput)
    }
  }
}
</script>

<style>
#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
