public class Solution {
    public int minDistance(String word1, String word2) {
        int m = word1.length(), n = word2.length();
        int[] pre = new int[n+1];
        for(int j = 0; j <= n; j++) pre[j] = j;
        for(int i = 1; i <= m; i++) {
            int[] cur = new int[n+1];
            cur[0] = i;
            for(int j = 1; j <= n; j++) {
               int temp = pre[j-1];
               if(word1.charAt(i-1) != word2.charAt(j-1)) temp++;
               cur[j] = Math.min(temp, Math.min(pre[j] + 1, cur[j-1] + 1));
            }
            pre = cur;  
        }
        return pre[n];
    }
}