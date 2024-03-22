public class Solution {
    public int lengthOfLongestSubstringTwoDistinct(String s) {
        int m = s.length();
        if(m == 0) return 0;
        
        //find the longest substring with at most 2 distinct chars starting from 0
        char ch1 = s.charAt(0);
        int len = 1; while(len < m && s.charAt(len) == ch1) len++;
        if(len == m) return len;
        char ch2 = s.charAt(len);
        while(len < m && (s.charAt(len) == ch1 || s.charAt(len) == ch2)) len++;
        if(len == m) return len;
        
        int start = 0, end = len;//note that start is inclusive and end is exclusive
        while(end < m) {
            ch1 = s.charAt(end - 1); ch2 = s.charAt(end);
            start = end - 1; while(start >= 0 && s.charAt(start) == ch1) start--;
            start++;
            while(end < m && (s.charAt(end) == ch1 || s.charAt(end) == ch2)) end++;
            len = Math.max(len, end - start); 
        }
        return len;
    }
}