package com.codewithmosh;

import java.text.NumberFormat;
import java.util.Scanner;

import javax.xml.transform.Source;

public class Java {
    
    public static void main(String[] args){
        // String result = NumberFormat.getPercentInstance().format(0.1);
        // System.out.println(result);

        Scanner scanner = new Scanner(System.in);
        System.out.print("Name : ");
        String name = scanner.nextLine().trim();
        System.out.println("You are " + name);
    }
}
