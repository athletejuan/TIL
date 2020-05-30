<template>
  <div class="todo-list">
    <h1>Todo</h1>
    <div class="card" v-for="todo in todos" :key="todo.id">
      <div class="card-body d-flex justify-content-between">
        <span @click="updateTodo(todo)" :class="{complete: todo.completed}">{{ todo.title }}</span>
        <span @click="deleteTodo(todo)">🗑</span>
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios'
export default {
  name: 'TodoList',
  props: {
    todos: Array
  },
  methods: {
    deleteTodo: function(todo){
      this.$session.start()
      const token = this.$session.get('jwt')
      const requestHeader = {
        headers: {
          Authorization: "JWT " + token
        }
      }
      axios.delete(`http://localhost:8000/api/v1/todos/${todo.id}/`, requestHeader)
      .then(res => {
        console.log(res)
        const targetTodo = this.todos.find(function(el){
          return el === todo
        })
        const idx = this.todos.indexOf(targetTodo)
        if (idx > -1) this.todos.splice(idx, 1)
      })
      .catch(e => {
        console.log(e)
      })
    },
    updateTodo: function(todo) {
      this.$session.start()
      const token = this.$session.get('jwt')
      const requestHeader = {
        headers: {
          Authorization: "JWT " + token
        }
      }
      const requestForm = new FormData()
      requestForm.append('completed', !todo.completed)
      requestForm.append('user', todo.user)
      requestForm.append('id', todo.id)
      requestForm.append('title', todo.title)
      
			// update를 위한 put 요청
      axios.put(`http://localhost:8000/api/v1/todos/${todo.id}/`, requestForm, requestHeader)
			// 요청 성공시 vue화면의 상태 변경
      .then(res => {
        console.log(res)
        todo.completed = !todo.completed
      })
      .catch(e => {
        console.log(e)
      })
    }
  }
}
</script>

<style>
.complete {
  text-decoration: line-through;
  color: rgb(112,112,112);
}
</style>