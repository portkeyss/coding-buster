public class Solution {
    public boolean isNumber(String s) {
        String str = s.trim();
        int len = str.length();
        //"   +(-) 123.456E(e)+(-)789   "
        int i = 0;
        if(i == len) return false;
        if(str.charAt(i) == '+' || str.charAt(i) == '-') i++;
        if(i == len) return false;
        
        boolean digit_exist = false;
        //iterate until '.' or 'E' or'e' or end
        while(i < len && str.charAt(i) >= '0' && str.charAt(i) <= '9') {i++; digit_exist = true;}
        if(i == len) return true;
        
        if(str.charAt(i) == '.') i++;
        while(i < len && str.charAt(i) >= '0' && str.charAt(i) <= '9') {i++; digit_exist = true;}
        if(!digit_exist) return false;
        if(i == len) return true;

        if(str.charAt(i) == 'e' || str.charAt(i) == 'E') i++;
        else return false;
        if(i == len) return false;
        if(str.charAt(i) == '+' || str.charAt(i) == '-') i++;
        if(i == len) return false;
        if(str.charAt(i) >= '0' && str.charAt(i) <= '9') i++;
        else return false;
        while(i < len && str.charAt(i) >= '0' && str.charAt(i) <= '9') i++;
        if(i == len) return true;
        return false;
    }
}