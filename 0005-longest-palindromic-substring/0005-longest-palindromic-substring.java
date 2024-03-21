public class Solution {
    public String longestPalindrome(String s) {
        int len = s.length();
        int max = 1;
        int start = 0; int end = 0;
        for(int i = 0; i < len && max < 2 * len - 2 * i - 1; i++) {
            int l = i;
            for(int r = i; r < len && r <= i+1 && s.charAt(l) == s.charAt(r); r++) {
                int j = l; int k = r;
                while(j > -1 && k < len && s.charAt(j) == s.charAt(k)) {j--;k++;}
                if(k - j - 1 > max) {max = k - j - 1; start = j+1; end = k-1;}
            }
        }
        return s.substring(start, end+1);
    }
}