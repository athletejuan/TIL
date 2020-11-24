<template>
  <div class="mylist">
    <ul v-for="(newMovie, idx) in commingsoon" :key="idx" :class='{ completed: newMovie.completed }'>
      <li v-if="newMovie.created">
        <span @click="updateMovieStatus(newMovie)">{{ newMovie.title }}</span>
        <button @click="editMovieTitle(newMovie)">edit</button>
        <button @click="deleteMovie(newMovie)">x</button>  
      </li>
      <li v-else>
        <input type="text" v-model="nowMovie" @keydown.enter="editComplete(newMovie)">
        <button @click="editComplete(newMovie)">edit</button>
      </li>
    </ul>
  </div>
</template>

<script>
import { mapState } from 'vuex'

export default {
  name: 'MyList',
  data: function () {
    return {
      nowMovie: ''
    }
  },
  methods: {
    updateMovieStatus: function (movie) {
      this.$store.dispatch('updateMovie', movie)
    },
    editMovieTitle: function (movie) {
      this.nowMovie = movie.title
      movie.created = false
    },
    editComplete: function (newMovie) {
      const movies = [newMovie, this.nowMovie]
      this.$store.dispatch('editMovie', movies)
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
button {
  margin-left: 5px;
}
span {
  font-weight: bold;
  font-size: 20px;
}
</style>