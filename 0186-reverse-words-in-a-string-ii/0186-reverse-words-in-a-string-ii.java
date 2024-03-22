public class Solution {
    public void reverseWords(char[] s) {
        int m = s.length;
        if(m == 0) return;
        reverseWords(s,0,m-1);
        int i = 0;
        while(i < m) {
            while(i < m && s[i] == ' ') i++;
            if(i == m) return;
            int j = i;
            while(j < m && s[j] != ' ') j++;
            reverseWords(s,i,j-1);
            i = j;
        }
    }
    private void reverseWords(char[] s, int start, int end) {
        while(start <= end) {
            char temp = s[start];
            s[start] = s[end];
            s[end] = temp;
            start++;end--;
        }
    }
}