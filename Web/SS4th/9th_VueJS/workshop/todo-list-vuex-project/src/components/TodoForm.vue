<template>
  <div>
    <input type="text" v-model="todoTitle" @keydown.enter="createTodo">
    <button @click="createTodo">+</button>
  </div>
</template>

<script>
export default {
  name: 'TodoForm',
  data: function () {
    return {
      todoTitle: '',
    }
  },
  methods: {
    createTodo: function () {
      // console.log('todo 생성!!')
      // this.$store.commit('CREATE_TODO', {
      //   title: this.todoTitle,
      //   completed: false
      // })
      // this.todoTitle = ''
      const todoItem = {
        title: this.todoTitle,
        completed: false,
      }
      this.$store.dispatch('createTodo', todoItem)
      this.todoTitle = ''
    }
  },
}
</script>

<style>

</style>