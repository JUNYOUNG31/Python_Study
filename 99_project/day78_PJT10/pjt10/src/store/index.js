import Vue from 'vue'
import Vuex from 'vuex'
import axios from 'axios'

Vue.use(Vuex)
export default new Vuex.Store({
  state: {
    movieCards: [],
    myMovieList: []
  },
  mutations: {
    LOAD_MOVIE_CARDS: function (state, results) {
      state.movieCards = results
    },
    CREATE_MOVIE_LIST: function (state, movieItem) {
      state.myMovieList.push(movieItem)
    },
    DELETE_MOVIE_LIST: function (state, movieItem) {
      const index = state.myMovieList.indexOf(movieItem)
      state.myMovieList.splice(index, 1)
    },
  },
  actions: {
    LoadMovieCards: function ({commit}) {
      axios({
        method: 'get',
        url: 'https://api.themoviedb.org/3/movie/top_rated',
        params: {
          api_key: '16d1729d729f6d8c5d36bfaba0aee1a6',
          language: 'ko-KR',
        }
      })
      .then((res) => {
        commit('LOAD_MOVIE_CARDS', res.data.results)
      })
    },
    createMovieList: function (context, movieItem) {
      context.commit('CREATE_MOVIE_LIST', movieItem)
    },
    deleteMovieList: function (context, movieItem) {
      context.commit('DELETE_MOVIE_LIST', movieItem)
    },    
  },
  modules: {
  }
})
