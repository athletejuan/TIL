<template>
  <div class="container">
    <TodoInput @input-change="addTodo"/>
    <TodoList :todos="todos" @checked="updateTodo" @clicked="deleteTodo"/>
  </div>
</template>

<script>
// @ is an alias to /src
import axios from 'axios'
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
      const requestForm = new FormData()
      requestForm.append('content', todo)

      axios.post('https://django-vue-todolist.herokuapp.com/api/v1/todos/', requestForm)
        .then(res => {
          console.log(res.data)
          this.todos.push(res.data)
        })
        .catch(e => {
          console.log(e)
        })
      console.log(this.todos)
    },
    updateTodo(todo) {
      todo.is_completed = !todo.is_completed
    },
    deleteTodo(selected_todo) {
      axios.delete(`https://django-vue-todolist.herokuapp.com/api/v1/todos/${selected_todo.id}`)
        .then(res => {
          console.log(res.data)
        })
        .catch(e => {
          console.log(e)
        })
      this.todos = this.todos.filter(todo=>{
          return todo.id !== selected_todo.id
        })
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
