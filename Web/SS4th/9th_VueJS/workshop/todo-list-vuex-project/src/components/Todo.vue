<template>
  <div>
    <div>
      <span :class="{ completed: todo.completed }" @click="updateTodoStatus">{{ todo.title }} </span>
      <button @click="deleteTodo">x</button>
    </div>
  </div>
</template>

<script>
export default {
  name: 'Todo',
  props: {
    todo: {
      type: Object,
    }
  },
  methods: {
    deleteTodo: function () {
      // this.$store.commit('DELETE_TODO', this.todo)
      this.$store.dispatch('deleteTodo', this.todo)
      // console.log('Delete!')
    },
    updateTodoStatus: function () {
      this.$store.dispatch('updateTodoStatus', this.todo)
      // console.log('Update')
    }
  }
}
</script>

<style scoped>
  .completed {
    text-decoration: line-through;
  }
</style>