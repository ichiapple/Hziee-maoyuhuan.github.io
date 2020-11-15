function check() {
    var name = $(".username").val()
    var password = $(".userpassword").val()

    // alert("name" + name)
    // alert("password" + password)

    if (name === "") {
        alert("用户名不能为空");
        $(".username").focus();
    } else if (password === "") {
        alert("密码不能为空")
        $(".userpassword").focus();
    } else if ("admin" === name && "root" === password) {
        alert("登陆成功")
        window.location = "https://hziee-maoyuhuan.github.io/index/index.html";
    } else {
        alert("用户名或密码错误")
        location.reload();
    }
}