package com.hziee.myh.base64;


import com.sun.org.apache.xml.internal.security.utils.Base64;

//当字节不够的时候需要使用=进行补齐 直到补成三个字节为止
public class base64 {
    public static void main(String[] args) {
        String str = "";
        str = "1";       //1表示一个字节 不够三个字节 则1变成了MQ 后面的空变成==
        System.out.println(Base64.encode(str.getBytes()));
        str = "12";
        System.out.println(Base64.encode(str.getBytes()));
        str = "123";
        System.out.println(Base64.encode(str.getBytes()));

        str = "你好";     //utf-8的情况下 一个中文三个字节
        System.out.println(Base64.encode(str.getBytes()));
    }

}
