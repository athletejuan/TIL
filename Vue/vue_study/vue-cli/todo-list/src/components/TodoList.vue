<template>
  <div>
    <h1>TodoList</h1>
    <ul>
      <li v-for="todo in todos" :key="todo.id" :class="{completed:todo.completed}">
        <input type="checkbox" v-model="todo.completed">
        {{ todo.content }}
      </li>
    </ul>
  </div>
</template>

<script>
export default {
  props: {
    todos: {
      type: Array,
      required: true
    }
  }
}
</script>

<style>
ul {
  display: inline-block;
  text-align: left;
}
.completed{
  text-decoration: line-through;
}
</style>