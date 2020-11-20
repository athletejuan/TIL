import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    commingsoon: []
  },
  mutations: {
    ADD_MOVIE: function (state, newMovie) {
      state.commingsoon.push(newMovie)
    },
    UPDATE_MOVIE: function (state, Movie) {
      state.commingsoon = state.commingsoon.map((movie) => {
        if (movie === Movie) {
          return { ...movie, completed: !movie.completed}
        }
        return movie
      })
    },
    DELETE_MOVIE: function (state, Movie) {
      const idx = state.commingsoon.indexOf(Movie)
      state.commingsoon.splice(idx, 1)
    }
  },
  actions: {
    addMovie: function ({ commit }, newMovie) {
      if (newMovie) {
        commit('ADD_MOVIE', newMovie)
      }
    },
    updateMovie: function ({ commit }, Movie) {
      commit('UPDATE_MOVIE', Movie)
    },
    deleteMovie: function ({ commit }, Movie) {
      commit('DELETE_MOVIE', Movie)
    },
    
  },
  modules: {
  }
})
