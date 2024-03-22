public class Solution {
    public String intToRoman(int num) {
        StringBuffer sb = new StringBuffer();
        int i, j;
        if(num >= 1000){
            i = num / 1000;
            for(int k = 0; k < i; k++) sb.append("M");
            num = num % 1000;
        }
        if(num >= 100){
            i = num / 100;
            if(i == 9) sb.append("CM");
            else if (i > 5) {
                sb.append("D");
                for(int k = 0; k < i-5; k++) sb.append("C");
            }
            else if (i == 5) sb.append("D");
            else if (i == 4) sb.append("CD");
            else {
                for(int k = 0; k < i; k++) sb.append("C");
            }
            num = num % 100;
        }
        if(num >= 10){
            i = num / 10;
            if(i == 9) sb.append("XC");
            else if (i > 5) {
                sb.append("L");
                for(int k = 0; k < i-5; k++) sb.append("X");
            }
            else if (i == 5) sb.append("L");
            else if (i == 4) sb.append("XL");
            else {
                for(int k = 0; k < i; k++) sb.append("X");
            }
            num = num % 10;
        }
        i = num;
        if(i == 9) sb.append("IX");
        else if (i > 5) {
            sb.append("V");
            for(int k = 0; k < i-5; k++) sb.append("I");
        }
        else if (i == 5) sb.append("V");
        else if (i == 4) sb.append("IV");
        else {
            for(int k = 0; k < i; k++) sb.append("I");
        }
        
        return sb.toString();
    }
}