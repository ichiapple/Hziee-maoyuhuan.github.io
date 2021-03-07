console.log("hello node.js")
let a = 123;
let b = 456;
console.log((a + b));

// 向外部暴露自己的属性需要添加export关键字
exports.x = "Hello"
exports.fn = function (){}