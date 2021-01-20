<template>
  <div class="todo-item">
    <label for="">
      <input type="checkbox" :checked="todoItem.completed" />
     {{todoItem.content}}
      <span class="check-button"></span>
    </label>
  </div>
</template>

<script>
export default {
  name: "TodoListItems",
  props:["todoItem"]
};
</script>

<style>
:root {
  --todo-item-background-color: white;
  --todo-item-text-color: #626262;
  --check-button-color: #b382f9;
}

/* 列表项 */
.todo-item {
  background: var(--todo-item-background-color);
  padding: 16px;
  border-radius: 8px;
  color: var(--todo-item-text-color);
}

.todo-item label {
  position: relative;
  display: flex;
  align-items: center;
  justify-content: start;
}

.todo-item label span.check-button {
  position: absolute;
  top: 0;
}

.todo-item label span.check-button::before,
.todo-item label span.check-button::after {
  content: "";
  display: block;
  position: absolute;
  width: 18px;
  height: 18px;
  border-radius: 50%;
}

.todo-item label span.check-button::before {
  border: 2px solid var(--check-button-color);
}

.todo-item label span.check-button::after {
  translate: 0.5s;
  background-color: var(--check-button-color);
  transform: translate(2px, 2px) scale(0.8);
  opacity: 0;
}

.todo-item input {
  margin-right: 16px;
  opacity: 0; /* 隐藏原生复选框 */
}

.todo-item input:checked + span.check-button::after {
  opacity: 1; /* 如果点击复选框则将其相邻的span元素设置为可见 */
}
</style>