<template>
  <div class="bg-success p-2" style="--bs-bg-opacity: .25;">
    <h1>MyMovieList</h1>
    <my-list-form></my-list-form>
    <my-list></my-list>
  </div>
</template>

<script>
import MyListForm from '@/components/MyListForm.vue'
import MyList from '@/components/MyList.vue'

export default {
  name: 'MyMovieList',
  components: {
    MyListForm,
    MyList
  }
}
</script>

<style>

</style>