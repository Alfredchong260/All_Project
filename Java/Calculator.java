package com.codewithmosh;

import java.text.NumberFormat;
import java.util.Scanner;

public class Calculator{

    public static void main(String[] args){
        final byte MONTH_IN_YEAR = 12;
        final byte PERCENT = 100;

        Scanner scanner = new Scanner(System.in);

        System.out.print("Principle : ");
        int principle = scanner.nextInt();

        Scanner scanner2 = new Scanner(System.in);

        System.out.print("Annual Interest Rate : ");
        float interest = scanner2.nextFloat();
        float monthlyInterest = interest / PERCENT / MONTH_IN_YEAR;

        Scanner scanner3 = new Scanner(System.in);

        System.out.print("Period (Years) : ");
        byte period = scanner3.nextByte();
        int NumberOfpayment = period * MONTH_IN_YEAR;

        double mortgage = principle * 
            (monthlyInterest * Math.pow(1 + monthlyInterest, NumberOfpayment)) / 
            (Math.pow(1 + monthlyInterest, NumberOfpayment) -1);


        String Formatmortgage = NumberFormat.getCurrencyInstance().format(mortgage);
        System.out.println("Mortgage : " + Formatmortgage);

    }
}
