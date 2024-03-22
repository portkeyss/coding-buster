public class Solution {
    public String shortestPalindrome(String s) {
        String sRev = (new StringBuffer(s)).reverse().toString();
        String l = s + "#" + sRev;
        int len = l.length();
        int[] lps = new int[len];//longest proper prefix which is also a suffix
        for(int i = 1; i < len; i++) {
            int j = lps[i - 1];
            while(j > 0 && l.charAt(i) != l.charAt(j)) j = lps[j-1];
            if(l.charAt(i) == l.charAt(j)) j++;
            lps[i] = j;
        }
        return sRev.substring(0,s.length() - lps[len - 1]) + s;
    }
}