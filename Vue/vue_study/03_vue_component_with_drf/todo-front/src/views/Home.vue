<template>
  <div class="home">
    <h1>Todo</h1>
    <!-- <img alt="Vue logo" src="../assets/logo.png">
    <HelloWorld msg="Welcome to Your Vue.js App"/> -->
    <TodoInput @createTodo="createTodo" />
    <TodoList :todos="todos"/>
  </div>
</template>

<script>
// @ is an alias to /src
// import HelloWorld from '@/components/HelloWorld.vue'
import router from '../router'
import TodoList from '@/components/TodoList.vue'
import TodoInput from '@/components/TodoInput.vue'

import axios from 'axios'
import jwtDecode from 'jwt-decode'

export default {
  name: 'Home',
  components: {
    TodoList,
    TodoInput
  },
  data() {
    return {
      todos: []
    }
  },
  mounted() {
    this.checkLoggedIn()
    this.getTodos()
  },
  methods: {
    checkLoggedIn() {
      this.$session.start()
      if (!this.$session.has("jwt")){
        router.push("/login")
      }
    },
    getTodos: function() {
      this.$session.start()
      const token = this.$session.get('jwt')
      const requestHeader = {
        headers: {
          Authorization: "JWT " + token
        }
      }
      const user_id = jwtDecode(token).user_id
      axios.get(`http://localhost:8000/api/v1/user/${user_id}/`, requestHeader)
      .then(res => {
        console.log(res)
        this.todos = res.data.todo_set
      })
      .catch(e => {
        console.log(e)
      })
    },
    createTodo: function(title) {
      this.$session.start()
      const token = this.$session.get('jwt')
      const requestHeader = {
        headers: {
          Authorization: "JWT " + token
        }
      }
      const user_id = jwtDecode(token).user_id

      // axios를 통해서 post요청으로 data를 보내기 위해서는 FormData로 만들어 보내야한다.
      const requestForm = new FormData()
      requestForm.append('user', user_id)
      requestForm.append('title', title)

      axios.post(`http://localhost:8000/api/v1/todos/`, requestForm, requestHeader)
      .then(res => {
        console.log(res)
        this.todos.push(res.data)
      })
      .catch(e => {
        console.log(e)
      })
    }
  }
}
</script>
