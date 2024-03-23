class Solution {
    public int countSubstrings(String s) {
        int count = 0;
        for(int i = 0; i < s.length(); i++) {
            for(int j = 0; i-j >=0 && i+j < s.length(); j++){//odd length substrings
                if(s.charAt(i-j) != s.charAt(i+j)) break;
                count++;
            }
            for(int j = 0; i-j >=0 && i+j+1 < s.length(); j++){//even length substrings
                if(s.charAt(i-j) != s.charAt(i+j+1)) break;
                count++;
            }
        }
        return count;
    }
}