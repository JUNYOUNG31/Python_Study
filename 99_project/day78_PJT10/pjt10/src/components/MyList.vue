<template>
  <div>
   <ul class="list-group">
    <my-list-item
      v-for="item in myMovieList"
      :key="item.title"
      :myMovie='item'
      >
    </my-list-item>
    </ul>
  </div>
</template>

<script>
import MyListItem from '@/components/MyListItem.vue'
import { mapState } from 'vuex'

export default {
  name: 'MyList',
  components: {
    MyListItem,
  },
  computed: {
    ...mapState([
      'myMovieList',
    ])
  }
}
</script>

<style>

</style>