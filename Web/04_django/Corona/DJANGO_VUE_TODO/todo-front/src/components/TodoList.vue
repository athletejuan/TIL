<template>
  <div>
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
    }
  }
}
</script>

<style>
.completed {
  text-decoration: line-through;
}
</style>