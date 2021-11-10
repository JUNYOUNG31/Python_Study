<template>
  <div class="border border-danger">
    <todo-list-item
      v-for="todo in todos"
      :key="todo.date"
      :todo="todo"
    >
    </todo-list-item>
  </div>
</template>

<script>
import { mapState } from 'vuex'
import TodoListItem from '@/components/TodoListItem'

export default {
  name: 'TodoList',
  components: {
    TodoListItem,
  },
  // 1번
  // computed: { 
  //   todos: function () { // computed 와 state 를 mapping
  //     return this.$store.state.todos
  //   }
  // }
  // 2번
  // computed: mapState([
  //   'todos',
  // ])
  // 최종
  computed: {
    ...mapState([
      'todos',
    ])
  }
}
</script>

<style>

</style>
