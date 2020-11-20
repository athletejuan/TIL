<template>
  <div>
    <input @keydown.enter="movieAdd" v-model.trim="movieTitle" type="text">
    <button @click="movieAdd">+</button>
  </div>
</template>

<script>
export default {
  name: 'MyListForm',
  data: function () {
    return {
      movieTitle: '',
    }
  },
  methods: {
    movieAdd: function () {
      const newMovie = {
        title: this.movieTitle,
        completed: false
      }
      this.$store.dispatch('addMovie', newMovie)
      this.movieTitle = ''
    }
  }
}
</script>

<style>

</style>