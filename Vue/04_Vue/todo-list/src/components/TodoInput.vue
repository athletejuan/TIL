<template>
  <div>
    <input type="text" v-model="todo" @keypress.enter="createTodo">
    <button @click="createTodo">등록</button>
  </div>
</template>

<script>
export default {
  name: 'TodoInput',
  data() {
    return {
      todo: '',
    }
  },
  methods: {
    createTodo() {
      if (this.todo) {
        this.$emit('create', {
          id: Date.now(),
          content: this.todo,
          isCompleted: false
        })
        this.todo = ''
      }
    }
  }
}
</script>

<style>

</style>