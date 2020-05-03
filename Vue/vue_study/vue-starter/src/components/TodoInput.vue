<template>
  <div>
    <h1>To Do List</h1>
    <input type="text" v-model="userInput">
    <input type="submit" v-on:click="newTodo">
  </div>
</template>

<script>
export default {
  data: function(){
    return {
      userInput: ''
    }
  },
  methods: {
    newTodo: function(){
      console.log(this.userInput)
      this.$emit('sendUserInput', this.userInput)
      this.userInput = ''
    }
  }
}
</script>

<style>

</style>