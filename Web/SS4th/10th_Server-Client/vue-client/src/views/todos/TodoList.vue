<template>
  <div>
    <ul>
      <li v-for="(todo, idx) in todos" :key="idx">
        <span @click="updateTodoStatus(todo)" :class="{ completed: todo.completed }">{{ todo.title }}</span>
        <button @click="deleteTodo(todo)" class="todo-btn">x</button>
      </li>
    </ul>
    <!-- <button @click="getTodos">Get Todos</button> -->
  </div>
</template>

<script>
import axios from 'axios'

const SERVER_URL = process.env.VUE_APP_SERVER_URL

export default {
  name: 'TodoList',
  data: function () {
    return {
      todos: [],
    }
  },
  methods: {
    setToken: function () {
      const token = localStorage.getItem('jwt')
      const config = {
        headers: {
          Authorization: `JWT ${token}`
        }
      }
      return config
    },
    getTodos: function () {
      const config = this.setToken()
      axios.get(`${SERVER_URL}`, config)
        .then(res => {
          // console.log(res)
          this.todos = res.data
        })
        .catch(err => {
          console.log(err)
        })
    },
    deleteTodo: function (todo) {
      const config = this.setToken()
      axios.delete(`${SERVER_URL}${todo.id}/`, config)
        .then((res) => {
          // console.log(res)
          const targetTodoIdx = this.todos.findIndex(function (todo) {
            return todo.id === res.data.id
          })
          this.todos.splice(targetTodoIdx, 1)
        })
        .catch(err => {
          console.log(err)
        })
    },
    updateTodoStatus: function (todo) {
      const config = this.setToken()
      const todoItem = {
        // title: this.title, completed: !todo.completed,
        ...todo,
        completed: !todo.completed
      }
      axios.put(`${SERVER_URL}${todo.id}/`, todoItem, config)
        .then(() => {
          // console.log(res)
          todo.completed = !todo.completed
        })
        .catch(err => {
          console.log(err)
        })
    }
  },
  created: function () {
    if (localStorage.getItem('jwt')) {
      this.getTodos()
    } else {
      this.$router.push({ name: 'Login' })
    }
  }
}
</script>

<style scoped>
  .todo-btn {
    margin-left: 10px;
  }
  .completed {
    text-decoration: line-through;
    color: rgb(112, 112, 112);
  }
</style>