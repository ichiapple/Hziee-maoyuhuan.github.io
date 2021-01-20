<template>
  <div class="todo-list">
    <!-- :todo-item="todo" 用于给子组件传递数据 -->
    <todo-list-items v-for="todo in todos" :key="todo.id" :todo-item="todo">
    </todo-list-items>
  </div>
</template>

<script>
import TodoListItems from "./TodoListItems";
export default {
  name: "TodoList",
  components: {
    TodoListItems,
  }, 
  props:["todos"],
};
</script>

<style>
/* todo列表 */
.todo-list {
  display: grid;
  row-gap: 14px; /* 列间距 */
}
</style>