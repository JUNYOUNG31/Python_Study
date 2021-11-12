<template>
  <div>
    <h1>Random</h1>
    <button @click="randomPick">Pick</button>
     <div class="mb-5 col">
        <div class="card border-secondary mx-auto mb-2" style="width:25rem;">
          <img :src="`https://image.tmdb.org/t/p/w500${pickMoviePoster}`" class="card-img-top mx-auto d-block" style="width: 20rem; height: 28rem;" alt="poster">
          <div class="card-body">
            <h4>{{ pickMovieTitle }}</h4>
            <!-- <p class="card-text text-center" style="overflow:hidden;white-space:nowrap;text-overflow:ellipsis;">{{ movieCard.overview }}</p> -->
          </div>
        </div>
      </div>    
  </div>
</template>

<script>
import _ from 'lodash'
import { mapState } from 'vuex'
export default {
  name: 'Random',
  data: function () {
    return {
      pickMovie : null,
      pickMovieTitle: null,
      pickMoviePoster: null,
    }
  },
  created: function () {
    this.$store.dispatch('LoadMovieCards')
  },
  computed: {
    ...mapState(['movieCards'])
  },
  methods: {
    randomPick: function () {
      const idx = _.random(this.movieCards.length - 1)
        this.pickMovie = this.movieCards[idx]
        this.pickMovieTitle = this.pickMovie.title
        this.pickMoviePoster = this.pickMovie.poster_path
    }
  }

  }


</script>

<style>

</style>