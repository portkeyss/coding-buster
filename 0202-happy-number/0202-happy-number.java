public class Solution {
    public boolean isHappy(int n) {
        if(n == 1) return true;//happy number always ends in 1
        if(n == 4) return false;//unhappy number always ends up cycling in (4, 16, 37, 58, 89, 145, 42, 20, 4...) see wiki for detailed explaination
        return isHappy(happy(n));
    }
    private int happy(int n) {
        String temp = n + "";
        int len = temp.length();
        int result = 0;
        for(int i = 0; i < len; i++) {
            int j = temp.charAt(i) - '0';
            result += j * j;
        }
        return result;
    }
}