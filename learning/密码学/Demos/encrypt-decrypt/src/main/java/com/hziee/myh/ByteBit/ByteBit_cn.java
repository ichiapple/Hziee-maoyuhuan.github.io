package com.hziee.myh.ByteBit;

import java.io.UnsupportedEncodingException;

// 根据编码的格式不一样,则编码的结果位数也是不一样的
// 如果是UTF-8 则一个中文对应的是三个字节 如果是GBK 则一个中文对应的是两个字节 可以在getBytes中设置 需要抛出异常
// 英文无所谓是UTF-8还是GBK
public class ByteBit_cn {
    public static void main(String[] args) throws UnsupportedEncodingException {
        String str = "你";
        byte[] bytes = str.getBytes("GBK");
        for (byte aByte : bytes) {
            System.out.println(aByte);      //一个中文对应的是三个字节(虽然不一定是三个)
            System.out.println(Integer.toBinaryString(aByte));
        }
    }
}
