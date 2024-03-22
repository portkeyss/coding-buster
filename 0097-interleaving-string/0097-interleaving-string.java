public class Solution {
    public boolean isInterleave(String s1, String s2, String s3) {
        if(s1.length() + s2.length() != s3.length()) return false;
        if(s1.equals("")) return s2.equals(s3);
        if(s2.equals("")) return s1.equals(s3);
        boolean[][] wrongWay = new boolean[s1.length()+1][s2.length()+1];
        return isInterleave(s1,s2,s3,wrongWay,0,0);
    }
    private boolean isInterleave(String s1, String s2, String s3, boolean[][] wrongWay, int curLen1, int curLen2) {
        if(curLen1 + curLen2 == s3.length()) return true;
        if(wrongWay[curLen1][curLen2]) return false;
        if(curLen1 < s1.length() && s1.charAt(curLen1) == s3.charAt(curLen1+curLen2) && isInterleave(s1,s2,s3,wrongWay,curLen1+1,curLen2)) return true;
        if(curLen2 < s2.length() && s2.charAt(curLen2) == s3.charAt(curLen1+curLen2) && isInterleave(s1,s2,s3,wrongWay,curLen1,curLen2+1)) return true;
        wrongWay[curLen1][curLen2] = true;
        return false;
    }
}