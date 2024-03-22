public class Solution {
    public int minCut(String s) {
        int len = s.length();
        int[] cuts = new int[len + 1];
        for(int i = 0; i <= len; i++) cuts[i] = i - 1;
        for(int i = 0; i < len; i++) {
            for(int j = 0; i - j >= 0 && i + j < len && s.charAt(i - j) == s.charAt(i + j); j++) {
                cuts[i + j + 1] = Math.min(cuts[i + j + 1], cuts[i - j] + 1);
            }//odd palindrome
            for(int j = 0; i - j >= 0 && i + 1 + j < len && s.charAt(i - j) == s.charAt(i + 1 + j); j++) {
                cuts[i +  1 + j + 1] = Math.min(cuts[i + 1 + j + 1], cuts[i - j] + 1);
            }//even palindrome
            //Note that the order of treating odd and even palindromes does not matter and whichever goes first does not affect the result
        }
        return cuts[len];
    }
}