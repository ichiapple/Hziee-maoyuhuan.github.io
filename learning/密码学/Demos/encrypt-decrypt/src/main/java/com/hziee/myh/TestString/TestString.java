package com.hziee.myh.TestString;

import com.sun.org.apache.xml.internal.security.exceptions.Base64DecodingException;
import com.sun.org.apache.xml.internal.security.utils.Base64;

public class TestString {
    //    toString和new String之间的区别
    public static void main(String[] args) throws Base64DecodingException {

//        表示base64的密文
        String str = "TU0jV0xBTiNVYys5bEdiUjZlNU45aHJ0bTdDQStBPT0jNjQ2NDY1Njk4IzM5OTkwMDAwMzAwMA==";

//        进行解码
        String rlt1 = new String(Base64.decode(str));
        String rlt2 = Base64.decode(str).toString();

//        输出测试
        System.out.println("new String方式" + rlt1);
        System.out.println("toString方式" + rlt2);

    }

}
