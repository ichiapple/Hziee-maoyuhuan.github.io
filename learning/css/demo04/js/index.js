
// 获取元素对象
const wordEle = document.querySelector('.word');
// 声明变量
let word = "Hello World.";


// // 1. 使用for+定时器实现
// for (let i = 0; i < word.length; i++) {
//     // 启动定时器
//     setTimeout(function (){
//         wordEle.innerHTML = word.substr(0,i)
//     },i*300)
// }

// 2. 使用你async和await实现
// 封装一个函数
function setText(text){     //为标签元素设置文本
    return new Promise((resolve, reject) => {
        setTimeout(()=>{
            wordEle.innerHTML = text;
            resolve();
        }, 200)

    })
}

// 声明一个函数
async function main(flag){
    if (flag){
        // 正向输入
        for (let i = 0; i <= word.length; i++) {
            await setText(word.substr(0,i))
        }
    }
    else {
        // 逆向删除
        for (let i = word.length; i >=0; i--) {
            await setText(word.substr(0,i))
        }
    }
    setTimeout(()=>{
        main(!flag)
    },1000)

}
main(true);