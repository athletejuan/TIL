<template>
  <div>
    <input v-model.trim="newTodo" @keydown.enter="createTodo" type="text">
    <button @click="createTodo">+</button>
  </div>
</template>

<script>
import axios from 'axios'

const SERVER_URL = process.env.VUE_APP_SERVER_URL

export default {
  name: 'CreateTodo',
  data: function () {
    return {
      newTodo: ''
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
    createTodo: function () {
      const config = this.setToken()
      const todoItem = {
        'title': this.newTodo
      }
      if (todoItem.title) {
        axios.post(`${SERVER_URL}`, todoItem, config)
          .then(() => {
            // this.todos.push(res.data)
            this.$router.push({ name: 'TodoList' })
          })
          .catch(err => {
            console.log(err)
          })
          this.newTodo = ''
      }
    }
  }
}
</script>

<style>

</style>