<template>
  <ul>
    <li v-for="todo in appTodos" v-bind:key="todo">{{ todo }}</li>
  </ul>
</template>

<script>
export default {
  data: function(){
    return {
      // todos: ['밥먹기','쉬기','공부하기']
    }
  },
  props: {
    appTodos: Array
  }
}
</script>

<style>

</style>