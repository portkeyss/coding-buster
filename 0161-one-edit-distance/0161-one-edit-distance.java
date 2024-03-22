public class Solution {
    public boolean isOneEditDistance(String s, String t) {
        int m = s.length(), n = t.length();
        if(m < n - 1 || m > n + 1) return false;
        if(m == n + 1) {
            int a = 0;
            while(a < n && s.charAt(a) == t.charAt(a)) a++;
            int b = m - 1;
            while(b > 0 && s.charAt(b) == t.charAt(b-1)) b--;
            if(a >= b) return true;
            else return false;
        }
        if(m == n - 1) {
            int a = 0;
            while(a < m && t.charAt(a) == s.charAt(a)) a++;
            int b = n - 1;
            while(b > 0 && t.charAt(b) == s.charAt(b-1)) b--;
            if(a >= b) return true;
            else return false;
        }
        //m == n
        int i = 0;
        while(i < n && s.charAt(i) == t.charAt(i)) i++;
        int j = m - 1;
        while(j >= 0 && s.charAt(j) == t.charAt(j)) j--;
        if(i == j) return true;
        return false;
    }
}