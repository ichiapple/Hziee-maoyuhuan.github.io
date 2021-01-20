
// components文件夹用于存放未来会存放的组件
// assets文件夹用于存放静态资源文件 (图片/视频)
// public文件夹用于存放打包生成的html文件的模板


// 用于写HTML代码
<template>
  <main>
    <div class="container">
      <h1>欢迎使用 Huan 待办事项</h1>

      <!-- tid用于设置当前todo的下标 使用addTodo处理事件 -->
      <todo-add :tid="todos.length" @add-todo="addTodo" />
      <todo-filter />
      <!-- 在template标签中,会自动拆解出value属性 -->
      <todo-list :todos="todos" />
    </div>
  </main>
</template>

// 写Vue的js部分
<script>
import TodoAdd from "./components/TodoAdd.vue";
import TodoFilter from "./components/TodoFilter.vue";
import TodoList from "./components/TodoList.vue";
import { ref } from "vue";

export default {
  name: "App",
  components: {
    TodoFilter,
    TodoAdd,
    TodoList,
  },
  setup() {
    // 使用ref或reactive封装的数据变化会更新,ref用于基本上数据类型 reactive用于复杂数据类型
    const todos = ref([]); // 先封装一个空数组作为默认
    const addTodo = (todo) => todos.value.push(todo); // 通过事件 接收一个todo参数,保存todo信息,保存到列表中
    return {
      // 以对象形式进行返回
      todos, // 使用ref包装的对象需要访问value属性才能拿到数据
      addTodo,
    };
  },
};
</script>

<style>
:root {
  /* 背景色 */
  --default-color: rgb(203, 210, 240);
  --shadow-color-1: rgba(0, 0, 0, 0.15);
  --contain-background-color: rgb(245, 246, 252);
  --title-color: #414873;
}

/* 初始化样式 */
* {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
  font-family: Helvetica, "PingFang SC", "Microsoft Yahei", sans-serif;
}

/* 整个页面 */
main {
  width: 100vw;
  min-height: 100vh;
  display: flex;
  align-items: center;
  justify-content: center;
  background-color: var(--default-color);
}

/* Todo应用容器 */
.container {
  width: 60%;
  max-width: 450px;
  box-shadow: 0 0 24px var(--shadow-color-1);
  border-radius: 24px;
  padding: 48px 28px;
  background-color: var(--contain-background-color);
}

/* 标题 */
h1 {
  margin: 24px 0;
  font-size: 28px;
  color: var(--title-color);
  text-align: center;
}
</style>
