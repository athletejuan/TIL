<template>
  <div>
    <TodoList :todos="todos" @checked="updateTodo"/>
    <TodoInput @create="createTodo"/>
  </div>
</template>

<script>
import TodoList from '../components/TodoList.vue'
import TodoInput from '../components/TodoInput.vue'

export default {
  name: 'TodoView',
  components: {
    TodoList,
    TodoInput,
  },
  data() {
    return {
      todos: [
        {
          id: 1,
          content: 'Django 복습',
          isCompleted: true
        },
        {
          id: 2,
          content: 'JavaScript 복습',
          isCompleted: true
        },
        {
          id: 3,
          content: 'Vue CLI 학습',
          isCompleted: false
        },
      ]
    }
  },
  methods: {
    updateTodo(todo) {
      todo.isCompleted = !todo.isCompleted
    },
    createTodo(todo) {
      this.todos.push(todo)
    }
  }
}
</script>

<style>

</style>