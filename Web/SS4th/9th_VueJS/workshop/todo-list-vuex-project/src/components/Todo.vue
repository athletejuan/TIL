<template>
  <div>
    <div>
      <span :class="{ completed: todo.completed }" @click="updateTodoStatus(todo)">{{ todo.title }} </span>
      <button @click="deleteTodo(todo)">x</button>
    </div>
  </div>
</template>

<script>
import { mapActions } from 'vuex'

export default {
  name: 'Todo',
  props: {
    todo: {
      type: Object,
    }
  },
  methods: {
    // deleteTodo: function () {
    //   // this.$store.commit('DELETE_TODO', this.todo)
    //   this.$store.dispatch('deleteTodo', this.todo)
    //   // console.log('Delete!')
    // },
    // updateTodoStatus: function () {
    //   this.$store.dispatch('updateTodoStatus', this.todo)
    //   // console.log('Update')
    // }
    ...mapActions([
      'deleteTodo',
      'updateTodoStatus',
    ])
  }
}
</script>

<style scoped>
  .completed {
    text-decoration: line-through;
  }
</style>