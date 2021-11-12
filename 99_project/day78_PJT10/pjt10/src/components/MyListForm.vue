<template>  
  <div class="input-group mb-3">
  <input type="text" 
    style=" border-radius: 25px 0px 0px 25px"
    v-model.trim="myMovieData"
    @keyup.enter="createmyMovie" 
    class="form-control" placeholder="Movie name" aria-label="Movie name" aria-describedby="button-addon2">
  <button
  style=" border-radius: 0px 25px 25px 0px"
  @click="createmyMovie"
  class="btn btn-outline-secondary" type="button" id="button-addon2">Add</button>
  </div>

</template>

<script>
export default {
  name: 'MyListForm',
  data: function () {
    return {
      myMovieData: null,
    }
  },
  methods: {
    createmyMovie: function () {
      const myMovieItem = {
        title: this.myMovieData,
        date: new Date().getTime(),
      }
      if (myMovieItem.title) {
        this.$store.dispatch('createMovieList', myMovieItem)
        }
      this.myMovieData = null
    }
  }
}
</script>

<style>

</style>