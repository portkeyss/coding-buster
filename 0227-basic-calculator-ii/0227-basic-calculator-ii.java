public class Solution {
    public int cur = 0;
    public int calculate(String s) {
        int result = 0; 
        int num = 0;
        int sign = 1;
        while(cur < s.length()) {
            char ch = s.charAt(cur);
            if(ch == ' ') {cur++; continue;}
            else if(ch == '+' || ch == '-') {
                result += sign * num;
                sign = ch == '+'? 1 : -1;
                cur++;
            }
            else if(ch == '*') {cur++; num *= parseInt(s);}
            else if(ch == '/') {cur++; num /= parseInt(s);}
            else {num = parseInt(s);}
        }
        result += sign * num;
        return result;
    }
    private int parseInt(String s) {
        int result = 0; 
        while(cur < s.length() && s.charAt(cur) == ' ') cur++;
        while(cur < s.length()) {
            char ch = s.charAt(cur);
            if(ch >= '0' && ch <= '9') result = 10 * result + ch - '0';
            else break;
            cur++;
        }
        return result;
    }
}