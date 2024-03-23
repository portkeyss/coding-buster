class Solution {
    public boolean validPalindrome(String s) {
        int i = 0;
        int j = s.length() - 1;
        while(i <= j){
            if(s.charAt(i) == s.charAt(j)){
                i++;
                j--;
            }else{
                break;
            }
        }
        if(i > j) return true;
        
        int i1 = i + 1;
        int j1 = j;
        while(i1 <= j1){
            if(s.charAt(i1) == s.charAt(j1)){
                i1++;
                j1--;
            }else{
                break;
            }
        }
        if(i1 > j1) return true;
        
        int i2 = i;
        int j2 = j - 1;
        while(i2 <= j2){
            if(s.charAt(i2) == s.charAt(j2)){
                i2++;
                j2--;
            }else{
                break;
            }
        }
        if(i2 > j2) return true;
        return false;
    }
}