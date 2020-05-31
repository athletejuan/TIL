<template>
  <div>
    <h1>TodoList</h1>
    <ul>
      <li v-for="todo in todos" :key="todo.id" :class="{ completed: todo.isCompleted }">
        <input type="checkbox" :checked="todo.isCompleted" @click="$emit('checked', todo)">
        {{ todo.content }}
      </li>
    </ul>
  </div>
</template>

<script>
export default {
  name: 'TodoList',
  props: {
    todos: {
      type: Array,
      required: true,
    }
  }
}
</script>

<style>
.completed {
  text-decoration: line-through;
}
</style>