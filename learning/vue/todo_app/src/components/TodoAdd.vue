<template>
  <div class="input-add">
    <!-- v-model 用于同步用户输入的内容 @keyup用于相应事件 -->
    <input
      type="text"
      name="todo"
      v-model="todoContent"
      @keyup.enter="emitAddTodo"
    />
    <button @click="emitAddTodo">
      <!-- 统一注册到同一个方法中  -->
      <!-- 用于显示加号, 从font-awesome中获取图标 -->
      <i class="plus"></i>
    </button>
  </div>
</template>

<script>
import { ref } from "vue";

export default {
  name: "TodoAdd",
  setup(props, context) {
    const todoContext = ref("");

    const emitAddTodo = () => {
      const todo = {
        // id值
        id: props.tid,
        // todo的内容
        content: todoContext.value,
        // 完成状态 默认未完成
        completed: false,
      };
      context.emit("add-todo", todo);
    // 输入框中内容清空
    todo.content.value = "";
    };

    return {
      todoContext,
      emitAddTodo,
    };
  },
};
</script>

<style>
:root {
  --input-add-box-shadow: rgba(0, 0, 0, 0.08);
  --input-add-text-color: #626262;
  --button-background: linear-gradient(#fff, #fff), linear-gradient(#fff, #fff);

  --add-button-color: linear-gradient(#c0a5f3, #7f95f7);
  --button-content-color: black;
}

/* 添加框 */
.input-add {
  position: relative;
  display: flex;
  align-items: center;
}

.input-add input {
  padding: 16px 60px 16px 22px;
  border-radius: 48px;
  border: none;
  outline: none;
  box-shadow: 0 0 14px var(--input-add-box-shadow);
  width: 100%;
  font-size: 16px;
  color: var(--input-add-text-color);
}

.input-add button {
  width: 46px;
  height: 46px;
  border-radius: 50%;
  background: var(--add-button-color);
  border: none;
  outline: none;
  color: var(--button-content-color);
  position: absolute;
  right: 4px;
  cursor: pointer;
}

.input-add button i {
  display: block; /* 要变成块级元素才能使宽高生效 */
  width: 100%;
  height: 100%;
  background: var(--button-background);
  background-size: 50% 2px, 2px 50%;
  background-position: center;
  background-repeat: no-repeat;
}
</style>