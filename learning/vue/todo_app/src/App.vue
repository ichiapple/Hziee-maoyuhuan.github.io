
// components文件夹用于存放未来会存放的组件
// assets文件夹用于存放静态资源文件 (图片/视频)
// public文件夹用于存放打包生成的html文件的模板


// 用于写HTML代码
<template>
  <!-- 
    <img alt="Vue logo" src="./assets/logo.png">
    <HelloWorld msg="Welcome to Your Vue.js App"/>
  -->
  <main>
    <div class="container">
      <h1>欢迎使用 Huan 待办事项</h1>
      <div class="input-add">
        <input type="text" name="todo" />
        <button>
          <!-- 用于显示加号, 从font-awesome中获取图标 -->
          <i class="plus"></i>
        </button>
      </div>

      <div class="filters">
        <span class="filter active">全部</span>
        <span class="filter">已完成</span>
        <span class="filter">未完成</span>
      </div>
      <div class="todo-list">
        <div class="todo-item">
          <label for="">
            <input type="checkbox" />
            Todo 1
            <span class="check-button"></span>
          </label>
        </div>
        <div class="todo-item">
          <label for="">
            <input type="checkbox" />
            Todo 2
            <span class="check-button"></span>
          </label>
        </div>
        <div class="todo-item">
          <label for="">
            <input type="checkbox" />
            Todo 3
            <span class="check-button"></span>
          </label>
        </div>
      </div>
    </div>
  </main>
</template>

// 写Vue的js部分
<script>
// import HelloWorld from "./components/HelloWorld.vue"; // 导入了components下的HelloWorld.vue组件

export default {
  name: "App",
  components: {
    // HelloWorld,
  },
};
</script>

// 写Vue的css部分
<style>
:root {
  /* 背景色 */
  --default-color: rgb(203, 210, 240);
  --add-button-color: gray;
  --shadow-color-1: rgba(0, 0, 0, 0.15);
  --contain-background-color: rgb(245, 246, 252);
  --title-color: #414873;
  --input-add-box-shadow: rgba(0, 0, 0, 0.08);
  --input-add-text-color: #626262;
  --add-button-color: linear-gradient(#c0a5f3, #7f95f7);
  --button-content-color: black;
  --filters-color: #c0c2ce;
  --actived-color: #6b729c;
  --todo-item-background-color: white;
  --todo-item-text-color: #626262;
  --check-button-color: #b382f9;
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
  background: linear-gradient(#fff, #fff), linear-gradient(#fff, #fff);
  background-size: 50% 2px, 2px 50%;
  background-position: center;
  background-repeat: no-repeat;
}

/* 过滤器 */
.filters {
  display: flex;
  margin: 24px 2px;
  color: var(--filters-color);
  font-size: 14px;
}

.filters .filter {
  margin-right: 14px;
  transition: 0.8s;
}

.filters .filter.active {
  color: var(--actived-color);
  transform: scale(1.2);
}

/* todo列表 */
.todo-list {
  display: grid;
  row-gap: 14px; /* 列间距 */
}

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
.todo-item label span.check-button::after{
  content: "";
  display: block;
  position: absolute;
  width: 18px;
  height: 18px;
  border-radius: 50%;
}

.todo-item label span.check-button::before{
border: 2px solid var(--check-button-color);
}

.todo-item label span.check-button::after{
  translate: 0.5s;
  background-color: var(--check-button-color);
  transform: translate(2px, 2px) scale(0.8);
  opacity: 0;
}

.todo-item input{
  margin-right: 16px;
  opacity: 0;   /* 隐藏原生复选框 */
}

.todo-item input:checked + span.check-button::after{
  opacity: 1; /* 如果点击复选框则将其相邻的span元素设置为可见 */
}
</style>
