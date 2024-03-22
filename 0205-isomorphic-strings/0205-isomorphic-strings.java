public class Solution {
    public boolean isIsomorphic(String s, String t) {
        int m = s.length();
        char[] image = new char[256];
        char[] backImage = new char[256];
        for(int i = 0; i < m; i++) {
            if(image[s.charAt(i)] == '\u0000') {
                if(backImage[t.charAt(i)] == '\u0000') {
                    image[s.charAt(i)] = t.charAt(i); backImage[t.charAt(i)] = s.charAt(i);
                }
                else return false;
            }
            else if(image[s.charAt(i)] != t.charAt(i)) return false;
        }
        return true;
    }
}