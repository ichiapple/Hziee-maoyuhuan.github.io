function check(){
    var name=document.username;
    var password=document.userpassword;
    if(name.value===""){
        alert("用户名不能为空");
        name.focus();
        return false;
    }
    if(password.value===""){
        alert("密码不能为空")
        password.focus();
        return false;
    }

    if ("admin"===name&&"root"===password){
        window.location = "https://hziee-maoyuhuan.github.io/index/index.html";
    }
    location.reload();
}