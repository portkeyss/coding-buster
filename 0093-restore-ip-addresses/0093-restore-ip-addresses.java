public class Solution {
    public List<String> restoreIpAddresses(String s) {
        List<String> l = new LinkedList<String>();
        for (int i = 0; i < 3 && i < s.length() - 3; i ++)
            for (int j = i + 1; j < i + 4 && j < s.length() - 2; j ++)
                for (int k = j + 1; k < j + 4 && k < s.length() - 1; k ++) {
                     String s1 = s.substring(0,i+1);
                     String s2 = s.substring(i+1,j+1);
                     String s3 = s.substring(j+1,k+1);
                     String s4 = s.substring(k+1,s.length());
                     if(pass(s1) && pass(s2) && pass(s3) && pass(s4)) 
                         l.add(s1 +"." + s2 + "." + s3 + "." + s4);
                }
        return l;
    }
    public boolean pass(String s) {
        if(  s.length() == 0 || s.length() > 3 ||(s.length() > 1 && s.charAt(0) == '0') ||Integer.parseInt(s) > 255) 
             return false;//note that s.length() > 3 is a must, however s.length() ==0 is not necessary,as it is precluded simply by construction of the indices order in the for loops
        else return true;
    }
}