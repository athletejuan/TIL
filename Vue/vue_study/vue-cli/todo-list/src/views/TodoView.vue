<template>
  <div>
    <TodoInput @createTodo="createTodo" />
    <TodoList :todos="todos" />
  </div>
</template>

<script>
import TodoList from '../components/TodoList.vue'
import TodoInput from '../components/TodoInput.vue'

export default {
  components: {
    TodoList,
    TodoInput
  },
  data() {
    return {
      todos: [
        {
          id: 1,
          content: 'Django 복습',
          completed: false
        },
        {
          id: 2,
          content: 'JavaScript 복습',
          completed: false
        },
        {
          id: 3,
          content: 'Vue CLI 학습',
          completed: false
        },
        // 'Django 복습',
        // 'JavaScript 복습',
        // 'Vue CLI 학습',
      ]
    }
  },
  methods: {
    createTodo(todo) {
      this.todos.push(todo)
    }
  }
}
</script>

<style>

</style>