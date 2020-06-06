<template>
  <div>
    <input @change="onInput" v-model="todo" type="text">
    <button @click="onInput">ADD</button>
  </div>
</template>

<script>
export default {
  name: 'TodoInput',
  data() {
    return {
      todo: ''
    }
  },
  methods: {
    onInput() {
      if (this.todo.trim()) {
        this.$emit('input-change', this.todo)
        // this.$emit('input-change', {
        //   id: Date.now(),
        //   content: this.todo,
        //   isCompleted: false,
        // })
        this.todo = ''
      }
    }
  }
}
</script>

<style>

</style>