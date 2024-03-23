class Solution {
    public boolean backspaceCompare(String S, String T) {//O(N) time and O(1) space
        int i = S.length() - 1;
        int j = T.length() - 1;
        int numOfBackspace1 = 0;
        int numOfBackspace2 = 0;
        while(i >= 0 || j >= 0){
            char ch1 = 'X';//any char not legally inside S or T
            char ch2 = 'X';
            for(; i >= 0; i--){
                if(S.charAt(i) == '#') numOfBackspace1++;
                else if(numOfBackspace1 > 0) numOfBackspace1--;
                else{
                    ch1 = S.charAt(i);
                    i--;//Note this step is often unintentianlly ignored, "break" breaks for-loop immediately, therefore index change in for-loop is not reached
                    break;
                }
            }
            for(; j >= 0; j--){
                if(T.charAt(j) == '#') numOfBackspace2++;
                else if(numOfBackspace2 > 0) numOfBackspace2--;
                else{
                    ch2 = T.charAt(j);
                    j--;
                    break;
                }
            }
            if(ch1 != ch2) return false;
        }
        return true;
    }
}