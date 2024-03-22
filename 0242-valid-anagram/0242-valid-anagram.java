public class Solution {
    public boolean isAnagram(String s, String t) {
        if(s.length() != t.length()) return false;
        int[] frequency = new int[256];
        int len = s.length();
        for(int i = 0; i < len; i++) {
            frequency[s.charAt(i)]++;
        }
        for(int i = 0; i < len; i++) {
            int j = t.charAt(i);
            frequency[j]--;
            if(frequency[j] < 0) return false;
        }
        return true;
    }
}