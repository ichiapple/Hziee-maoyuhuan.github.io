# Bootstrap

>   Bootstrap中文网: https://www.bootcss.com/  使用Bootstrap3版本,因为比较稳定

## 主要内容

<img src="C:\Users\MYH\AppData\Roaming\Typora\typora-user-images\image-20210121041211766.png" alt="image-20210121041211766"/>

## Bootstrap的安装和使用

### Bootstrap介绍

>   官网: http://getbootstrap.com/
>
>   中文网: http://www.bootcss.com/

-   Bootstrap是一套现成的CSS样式集合 由两个推特员工开发出来的
-   Bootstrap是最受欢迎的前端框架 用于开发响应式布局,移动设备优先的web项目
-   Bootstrap是一套易用,优雅,灵活,可扩展的前端工具集,在github上进行了开源

### Bootstrap特点

-   简洁美观 直观 强悍 前端开发工具集 让web开发更加简单快速
-   友好的学习曲线 卓越兼容性 12列网格 样式向导文档
-   自定义jQuery插件 完整类库 Bootstrap3基于Less Bootstrap4基于Sass的CSS预处理技术
-   Bootstrap响应式布局,让一个网页可以兼容不同分辨率的设备,给用户更好的体验
-   丰富的组件

### 下载和使用

-   下载 

    >   下载地址: http://v3.bootcss.com/getting-started/

-   下载完成后

    -   拷贝dist/css的bootstrap.min.css到项目css下
    -   拷贝dist/js的bootstrap.min.js到项目js下

-   下载jQuery.js

    >   下载地址: http://jquery.com

-   HTML模板

    ```html
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <!-- 使用X-UA-Compatible来设置IE浏览器的兼容模式 最新的渲染模式 -->
        <meta http-equiv="X-UA-Compatible" content="IE=edge">
        <!--
            viewport表示用户是否可以缩放页面    
            width指定视区逻辑宽度
            device-width指示视区宽度应该为设备宽度
            initial-scale指令设置web页面的初始缩放比例
            initial-scale=1展示未经缩放的页面
        -->
        <meta name="viewport" content="width=device-width, initial-scale=1">
        <title>BootStrap标准模板</title>
        <link rel="stylesheet" href="css/bootstrap.min.css">
    </head>
    <body>
        <h1>Hello bootstrap.</h1>
        <!-- 使用bootstrap的插件前必须先引入jQuery -->
        <script src="js/jquery-3.5.1.js"></script>
        <!-- 包括所有bootstrap的js插件或者可以根据需要使用的js插件进行调用 -->
        <script src="bootstrap.min.js"></script>
    </body>
    </html>
    ```

    -   为了表示模板完整性引入了jQuery 如果没用到可以不用引入该js文件

-   参考API

## 布局容器和栅格网格系统

## 常用样式

## Bootstrap插件