<template>
  <div class="home">
    <h1>Home</h1> 
      <div class="container-fluid">
        <div class="row">
          <movie-card 
            v-for="movieCard in movieCards"
            :key="movieCard.id"
            :movieCard="movieCard"
            >
          </movie-card>    
    </div>
  </div>
</div>
</template>

<script>
import MovieCard from '@/components/MovieCard.vue'
import { mapState } from 'vuex'

export default {
  name: 'Home',
  components: {
    MovieCard,
  },
  created: function () {
    this.$store.dispatch('LoadMovieCards')
  },
  computed: {
    ...mapState(['movieCards'])
  }
}
</script>
