from turtle import *
color("yellow","pink")
begin_fill()
while True:
    forward(200)
    right(144)      # 一个角36度
    if(abs(pos())<1):       # 绕一周然后退出
        break
end_fill()
done()