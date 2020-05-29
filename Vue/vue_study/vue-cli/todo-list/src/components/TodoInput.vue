<template>
  <div>
    <input type="text" @keyup.enter="createTodo" v-model="todo">
    <button @click="createTodo">등록</button>
  </div>
</template>

<script>
export default {
  data() {
    return {
      todo: []
    }
  },
  methods: {
    createTodo() {
      if (this.todo) {
        this.$emit('createTodo', {
              id: Date.now(),
              content: this.todo,
              completed: false,
            })
        this.todo = ''
      }
    }
  }
}
</script>

<style>

</style>