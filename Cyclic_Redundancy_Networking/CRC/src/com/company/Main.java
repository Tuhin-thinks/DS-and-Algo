package com.company;

import java.util.Scanner;

public class Main {

    static String compare(String a, String b){
        StringBuilder res = new StringBuilder();

        int size = Math.min(a.length(), b.length());

        for (int i = 0; i < size; i++) {
            char elem1 = a.charAt(i);
            char elem2 = b.charAt(i);

            if (elem1 == elem2){
                res.append('0');
            }
            else
                res.append('1');
        }
        return res.toString();
    }

    static String modify_dividend(String dividend, int len_divisor){
        StringBuilder new_dividend;
        new_dividend = new StringBuilder(dividend);
        new_dividend.append("0".repeat(len_divisor-1));
        return new_dividend.toString();
    }

    public static void main(String[] args) {
        int len_divisor, len_dividend, len_crc, pointer_pos = 0;
        String rem = "";
        StringBuilder quotient = new StringBuilder();
        StringBuilder compare_a = new StringBuilder();
        String last_rem;
        boolean first_iteration = true;
        Scanner sc = new Scanner(System.in);
        System.out.println("\nWant to check or find errors in CRC ? \n\t1. Find CRC and data to be transmitted.\n\t2. Check errors in transmitted data.");
        int mode = Integer.parseInt(sc.nextLine());

        System.out.print("Enter the data:");
        String dividend = sc.nextLine();

        System.out.print("Enter the key:");
        String divisor = sc.nextLine();

        len_divisor = divisor.length();
        len_crc = len_divisor - 1;

        if (mode == 1){  // this mode to find the CRC and the encoded data to be transmitted
            dividend = modify_dividend(dividend, len_divisor);
        }
        len_dividend = dividend.length();

        if (mode == 1)
            System.out.println("updated dividend:"+ dividend +", divisor:"+ divisor +";\n");

        int remaining_digits_count;
        String chunk, elem_now;

        while (pointer_pos < len_dividend){
//            remaining_digits_count = ;
            if (((len_dividend - pointer_pos) + compare_a.toString().length()) < len_divisor){
                chunk = dividend.substring(pointer_pos);
                quotient.append("0".repeat(chunk.length() - 1));
                rem = compare_a.toString() + chunk;
//                System.out.print("\tmodified here...");
                break;
            }
//            System.out.print("pointer pos:"+ pointer_pos +"  ");

            if (first_iteration){
                elem_now = dividend.substring(0, len_divisor);
                pointer_pos = len_divisor - 1;
                first_iteration = false;
            }
            else
                elem_now = String.valueOf(dividend.charAt(pointer_pos));

            compare_a.append(elem_now);
            System.out.print("compare_a="+compare_a + "  ");

            if (compare_a.length() == len_divisor){
                last_rem = compare(compare_a.toString(), divisor);
                compare_a = new StringBuilder(String.valueOf(Integer.parseInt(last_rem)));
                quotient.append('1');
                if (compare_a.toString().equals("0"))
                    compare_a = new StringBuilder();
                rem = last_rem;
            }
            else
                quotient.append('0');

            System.out.println("rem: "+ Integer.parseInt(rem) +"");
            pointer_pos += 1;
        }

        System.out.println("\nFinal remainder: "+ rem +", Quotient: "+ quotient +"");

        String final_rem = rem.substring(rem.length() - len_crc);


        String substring_dividend = dividend.substring(0, dividend.length() - len_crc);
        if (mode == 1){
            System.out.println("CRC:"+ final_rem +"");
            String data_to_transmit = substring_dividend + final_rem;
            System.out.println("Data to be transmitted: "+ data_to_transmit +"");
        }
        else{
            if (Integer.parseInt(final_rem) == 0){
                System.out.println("No error in data transmission");
                System.out.println("Actual data: "+ substring_dividend +"");
            }
            else
                System.out.println("Error in data transmission, final reminder: "+ final_rem +"");
        }
    }
}
