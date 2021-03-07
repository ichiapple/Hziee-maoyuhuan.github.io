/*
    模块化: 在js中 一个js文件就是一个模块
    每一个js文件(模块)都是运行在一个独立的函数中 有各自的作用域而非全局作用域
    模块之间调用都是看不到对方的变量
*/

console.log("Demo02.js is run.")

// 通过require函数引入外部模块 引入后回返回一个对象 代表引入的模块
let md = require("./01. helo node");  // 传递一个路径作为函数,如果使用相对路径需要用.或者..开头
console.log(md.a);  // undefined
console.log(md.x);  // 可以访问
console.log(md);