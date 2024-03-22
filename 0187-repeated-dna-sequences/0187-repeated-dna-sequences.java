import java.util.*;
public class Solution {
    public List<String> findRepeatedDnaSequences(String s) {
        List<String> result = new ArrayList<String>();
        int len = s.length();
        if(len <= 10) return result;
        Hashtable<Integer,Boolean> ht = new Hashtable<Integer,Boolean>();
        for(int i = 0; i <= len - 10; i++) {
            String tempStr = s.substring(i,i+10);
            int tempInt = stringToInt(tempStr);
            if(!ht.containsKey(tempInt)) ht.put(tempInt,false);
            else if(!ht.get(tempInt)) {ht.put(tempInt,true); result.add(tempStr);}
        }
        return result;
    }
    private int stringToInt(String s) {
        int strInt = 0,len = s.length();
        for(int i = 0; i < len; i++) {
            strInt *= 4; strInt += charToInt(s.charAt(i));
        }
        return strInt;
    }
    private int charToInt(char c) {
        switch(c) {
            case 'A': return 0;
            case 'C': return 1;
            case 'G': return 2;
            case 'T': return 3;
            default: return -1;
        }
    }
    /*private String intToString(int i) {
        StringBuffer sb = new StringBuffer();
        while(i != 0) {
            i/4
      
            sb.append();
        }
        return sb.toString();
    }
    private int charToInt(char c) {
        switch(c) {
            case 0: 'A';
            case 1: 'C';
            case 2: 'G';
            case 3: 'T';
            default: '\uFDEF';
        }
    }*/
}