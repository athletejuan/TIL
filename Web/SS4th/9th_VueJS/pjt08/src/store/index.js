import Vue from 'vue'
import Vuex from 'vuex'
import createPersistedState from 'vuex-persistedstate'

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    commingsoon: []
  },
  mutations: {
    ADD_MOVIE: function (state, newMovie) {
      state.commingsoon.push(newMovie)
    },
    EDIT_MOVIE: function (state, Movie) {
      state.commingsoon = state.commingsoon.map((movie) => {
        if (movie === Movie[0]) {
          return { ...movie, title: Movie[1], created: true}
        }
        return movie
      })
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
    editMovie: function ({ commit }, Movie) {
      commit('EDIT_MOVIE', Movie)
    },
    updateMovie: function ({ commit }, Movie) {
      commit('UPDATE_MOVIE', Movie)
    },
    deleteMovie: function ({ commit }, Movie) {
      commit('DELETE_MOVIE', Movie)
    },
    
  },
  modules: {
  },
  plugins: [
    createPersistedState(),
  ]
})
