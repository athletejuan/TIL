<template>
  <div class="container">
    <TodoInput @input-change="addTodo"/>
    <TodoList :todos="todos" @checked="updateTodo"/>
  </div>
</template>

<script>
// @ is an alias to /src
import TodoInput from '@/components/TodoInput.vue'
import TodoList from '@/components/TodoList.vue'

export default {
  name: 'Todo',
  components: {
    TodoList,
    TodoInput,
  },
  data() {
    return {
      todos: []
    }
  },
  methods: {
    addTodo(todo) {
      this.todos.push(todo)
    },
    updateTodo(todo) {
      todo.isCompleted = !todo.isCompleted
    }
  }
}
</script>

<style>
ul {
  display: inline-block;
  text-align: left;
}
</style>
