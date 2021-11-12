<template>
  <div>
    <li class="list-group-item list-group-item-secondary">{{ myMovie.title }}
      <button @click="deleteMovieList(myMovie)" class="btn btn-outline-success">Delete</button>
    </li>
  </div>
</template>

<script>
import { mapActions } from 'vuex'
export default {
  name: 'MyListItem',
  props: {
    myMovie: {
      type: Object,
    }
  },
  methods: {
    ...mapActions([
      'deleteMovieList'
    ])
  }
}
</script>

<style>

</style>