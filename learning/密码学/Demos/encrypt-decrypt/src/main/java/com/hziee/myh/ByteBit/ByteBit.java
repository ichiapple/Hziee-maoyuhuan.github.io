package com.hziee.myh.ByteBit;

public class ByteBit {
    public static void main(String[] args) {
        String a = "a";
        byte[] bytes = a.getBytes();
        for (byte aByte : bytes) {
            int b = aByte;
            System.out.println(b);
            System.out.println(Integer.toBinaryString(b));
        }
    }


}
