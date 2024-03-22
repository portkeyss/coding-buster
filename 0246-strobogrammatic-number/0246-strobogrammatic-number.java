class Solution {
    public boolean isStrobogrammatic(String num) {
        int len = num.length();
        for(int i = 0; i <= (len - 1)/2; i++){
            char ch = num.charAt(i);
            if(ch == '6') {
                if(num.charAt(len - 1 - i) != '9') return false;
            }else if(ch == '9') {
                if(num.charAt(len - 1 - i) != '6') return false;
            }else if(ch == '8') {
                if(num.charAt(len - 1 - i) != '8') return false;
            }else if(ch == '0') {
                if(num.charAt(len - 1 - i) != '0') return false;
            }else if(ch == '1') {
                if(num.charAt(len - 1 - i) != '1') return false;
            }else{
                return false;
            }
        }
        return true;
    }
}