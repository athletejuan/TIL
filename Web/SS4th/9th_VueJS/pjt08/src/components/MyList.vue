<template>
  <div class="mylist">
    <li v-for="(newMovie, idx) in commingsoon" :key="idx" :class='{ completed: newMovie.completed }'>
      <span @click="updateMovieStatus(newMovie)">{{ newMovie.title }}</span>
      <button @click="deleteMovie(newMovie)">x</button>  
    </li>
  </div>
</template>

<script>
import { mapState } from 'vuex'

export default {
  name: 'MyList',
  methods: {
    updateMovieStatus: function (movie) {
      this.$store.dispatch('updateMovie', movie)
    },
    deleteMovie: function (movie) {
      this.$store.dispatch('deleteMovie', movie)
    }
  },
  computed: {
    ...mapState([
      'commingsoon',
    ])
  }
}
</script>

<style>
.mylist {
  margin-top: 10px;
}
.completed {
  text-decoration: line-through;
  color: rgb(112, 112, 112);
}
</style>