public class Solution {
    public int numDecodings(String s) {
        int len = s.length();
        if(len == 0) return 0;
        
        //Initialize the counting values
        int prepre = 1, pre = 1, cur = 1;
        if(s.charAt(0) == '0') return 0;
        
        for(int i = 1; i < len; i++) { //Each step counts the number of possible decode ways that ends in this character in s
            if(s.charAt(i) == '0') {
                if(s.charAt(i-1) == '1'  || s.charAt(i-1) == '2') cur = prepre;
                else return 0;
            }
            else if(s.charAt(i - 1) == '1' || (s.charAt(i-1) == '2' && s.charAt(i) >= '1' && s.charAt(i) <= '6')) 
                cur = prepre + pre;
            else cur = pre;
            prepre = pre;
            pre = cur;
        }
        return cur;
    }
}