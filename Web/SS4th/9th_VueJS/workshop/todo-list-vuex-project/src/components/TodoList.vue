<template>
  <div>
    <Todo v-for="(todo, idx) in todos" :key="idx" :todo="todo" />
  </div>
</template>

<script>
import { mapState } from 'vuex'
import Todo from './Todo'

export default {
  name: 'TodoList',
  components: {
    Todo,
  },
  computed: {
    // todos: function () {
    //   return this.$store.state.todos
    // }
    ...mapState([
      'todos',
    ])
  }
}
</script>

<style>

</style>