<template>
  <div class="todo-input">
    <div class="input-group mb-3">
      <input type="text" class="form-control" v-model="title" @keyup.enter="createTodo()">
      <span class="input-group-btn">
        <button class="btn btn-primary" @click="createTodo()">+</button>
      </span>
    </div>
  </div>
</template>

<script>
export default {
  name: 'TodoInput',
  data: () => {
    return {
      title: ''
    }
  },
  methods: {
    createTodo: function() {
      this.$emit('createTodo', this.title)
      this.title = ''
    }
  }
}
</script>

<style>

</style>