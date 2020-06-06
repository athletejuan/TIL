<template>
  <div>
    <ul>
      <li v-for="todo in todos" :key="todo.id" :class="{ completed: todo.is_completed }">
        <input type="checkbox" :checked="todo.is_completed" @click="$emit('checked', todo)">
        {{ todo.content }}
        <button @click="$emit('clicked', todo)">x</button>
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