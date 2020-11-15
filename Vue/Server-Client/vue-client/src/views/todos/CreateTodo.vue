<template>
  <div>
    <input type="text" v-model.trim="title" @keydown.enter="createTodo">
    <button @click="createTodo">+</button>
  </div>
</template>

<script>
const SERVER_URL = process.env.VUE_APP_SERVER_URL
import axios from 'axios'

export default {
  name: 'CreateTodo',
  data: function () {
    return {
      title: '',
    }
  },
  methods: {
    createTodo: function () {
      const todoItem = {
        title: this.title,
      }

      if (todoItem.title) {
      axios.post(`${SERVER_URL}/`, todoItem)
        .then(() => {
          // console.log(res)
          this.$router.push({ name: 'TodoList' })
        })
        .catch((err) => {
          console.log(err)
        })
        this.title = ''
      }
    }
  }
}
</script>

<style>

</style>