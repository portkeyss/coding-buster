public class Solution {
    public int compareVersion(String version1, String version2) {
        int i = 0; int j = 0;
        int len1 = version1.length(); int len2 = version2.length();
        while(i < len1 && j < len2) {
            int start1 = i;int start2 = j;
            while(i < len1 && version1.charAt(i) != '.') i++;
            while(j < len2 && version2.charAt(j) != '.') j++;
            int rev1 = Integer.valueOf(version1.substring(start1,i)); 
            int rev2 = Integer.valueOf(version2.substring(start2,j));
            int dif = rev1 - rev2;
            if(dif < 0) return -1;
            else if(dif > 0) return 1;
            if(i < len1) i++; 
            if(j < len2) j++;
        }
        if(i == len1 && j == len2) return 0;
        else if(i < len1) {
            while( i < len1) {char ch = version1.charAt(i);if(ch == '0' || ch == '.') i++; else break;}
            if(i == len1) return 0;
            else return 1;
        }
        else {
            while( j < len2) {char ch = version2.charAt(j);if(ch == '0' || ch == '.') j++; else break;}
            if(j == len2) return 0;
            else return -1;
        }
    }
}