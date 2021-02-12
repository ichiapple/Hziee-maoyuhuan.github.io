package com.hziee.myh.desaes;

import com.sun.org.apache.xml.internal.security.exceptions.Base64DecodingException;
import com.sun.org.apache.xml.internal.security.utils.Base64;

import javax.crypto.BadPaddingException;
import javax.crypto.Cipher;
import javax.crypto.IllegalBlockSizeException;
import javax.crypto.NoSuchPaddingException;
import javax.crypto.spec.SecretKeySpec;
import java.security.InvalidKeyException;
import java.security.NoSuchAlgorithmException;

// 具体可以查看jdk8的说明文档
public class DesDemo {

    //    对称加密
    public static void main(String[] args) throws NoSuchPaddingException, NoSuchAlgorithmException, InvalidKeyException, BadPaddingException, IllegalBlockSizeException, Base64DecodingException {
//        原文
        String input = "你好";
//        定义密钥key
        String key = "12345678";        // 如果使用DES进行加密则密钥必须为8字节
//        定义算法
        String transformation = "DES";
//        加密类型
        String algorithm = "DES";

        System.out.println("原文:" + input);

        String password = getPassword(input, key, transformation, algorithm);       //调用方法获得密文

        System.out.println("加密:" + password);       //输出密文

        String string = getString(password, key, transformation, algorithm);        //调用方法获得明文

        System.out.println("解密:" + string);         //输出明文
    }

    private static String getPassword(String input, String key, String transformation, String algorithm) throws NoSuchAlgorithmException, NoSuchPaddingException, InvalidKeyException, IllegalBlockSizeException, BadPaddingException {

        //        创建加密规则 加密的文本字节码和加密的类型(算法)
        SecretKeySpec secretKeySpec = new SecretKeySpec(key.getBytes(), algorithm);
        //        Cipher是一个用于加密解密的对象 构成了Java加密扩展框架的核心
        Cipher cipher = Cipher.getInstance(transformation);
//        加密初始化 参数为模式和规则
//        模式有DECRYPT_MODE加密模式 和 ENCRYPT_MODE解密模式
        cipher.init(Cipher.ENCRYPT_MODE, secretKeySpec);
//        调用加密方法
        return getBase64String(cipher.doFinal(input.getBytes()));
    }

    private static String getString(String password, String key, String transformation, String algorithm) throws NoSuchAlgorithmException, NoSuchPaddingException, InvalidKeyException, IllegalBlockSizeException, BadPaddingException, Base64DecodingException {

        //        创建加密规则 加密的文本字节码和加密的类型(算法)
        SecretKeySpec secretKeySpec = new SecretKeySpec(key.getBytes(), algorithm);
        //        Cipher是一个用于加密解密的对象 构成了Java加密扩展框架的核心
        Cipher cipher = Cipher.getInstance(transformation);
//        加密初始化 参数为模式和规则
//        模式有DECRYPT_MODE加密模式 和 ENCRYPT_MODE解密模式
        cipher.init(Cipher.DECRYPT_MODE, secretKeySpec);
//        调用解密方法
        byte[] bytes = cipher.doFinal(getDecBase64String(password));

        return new String(bytes);

    }

    private static byte[] getDecBase64String(String password) throws Base64DecodingException {
        return Base64.decode(password);
    }

    private static String getBase64String(byte[] password) {
        //        需要结合base64进行使用
        return Base64.encode(password);
    }

    private static void testPasswordUsingByteArr(byte[] password) {
        for (byte b : password) {
            System.out.println(b);      //打印结果中有负数(不在ascii编码表上,所以出现了乱码)
        }
        System.out.println(new String(password));       // 如果直接打印密文会出现乱码(因为出现了不在ascii编码表上的字符)
    }       // 进行测试
}
