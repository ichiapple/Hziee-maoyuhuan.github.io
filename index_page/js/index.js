// 获取元素对象
const wordEle = document.querySelector('.word');
// 声明变量
let word = "Hello World.";

// 使用async和await实现
// 封装一个函数
function setText(text) { //为标签元素设置文本
    return new Promise((resolve, reject) => {
        setTimeout(() => {
            wordEle.innerHTML = text;
            resolve();
        }, 200)

    })
}

// 声明一个函数
async function main() {
    for (let i = 0; i <= word.length; i++) {
        await setText(word.substr(0, i))
    }
}
main();