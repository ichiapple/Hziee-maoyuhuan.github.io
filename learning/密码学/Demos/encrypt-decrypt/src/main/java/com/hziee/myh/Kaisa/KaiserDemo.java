package com.hziee.myh.Kaisa;

//凯撒加密
public class KaiserDemo {
    public static void main(String[] args) {
//        定义原文
        String input = "Hello World!";

//        如果我们需要把原文向右移动三位
        int key = 3;        //密钥设置为3

//        抽取方法快捷键 Ctrl + Alt + M
        String s = encryptKaiser(input, key);

        System.out.println("密文为:" + s);      //打印输出

        s = decryptKaiser(s, key);

        System.out.println("解密结果为:" + s);

        System.out.println("凯撒加密解密结束..");
    }

    private static String decryptKaiser(String s, int key) {        //s是密文 key是密钥
        //        新建一个StringBuilder用于存储输出的字符串
        StringBuilder stringBuilder = new StringBuilder();
        //        把字符串变成字节数组
        char[] chars = s.toCharArray();
        for (char aChar : chars) {
            int b = aChar;
            b -= key;
            stringBuilder.append((char) b);     //在stringBuilder后面进行追加
        }
        return stringBuilder.toString();
    }

    private static String encryptKaiser(String input, int key) {
        //        新建一个StringBuilder用于存储输出的字符串
        StringBuilder stringBuilder = new StringBuilder();
        //        把字符串变成字节数组
        char[] chars = input.toCharArray();
        for (char aChar : chars) {
            int b = aChar;
            b += key;
            stringBuilder.append((char) b);     //在stringBuilder后面进行追加
        }
        return stringBuilder.toString();
    }


}
