public class Solution {
    public String largestNumber(int[] num) {
        int len = num.length;
        String[] numStr = new String[len];
        for(int i = 0; i < len; i++) {
            numStr[i] = String.valueOf(num[i]);
        }
        Arrays.sort(numStr,new LargeNumComparator());
        if(numStr[len - 1].equals("0"))  return "0";
        StringBuilder sb = new StringBuilder();
        for(int i = len-1; i >= 0; i--) {
            sb.append(numStr[i]);
        }
        return sb.toString();
    }
    
    private class LargeNumComparator implements Comparator<String> {
        public int compare(String s1, String s2) {
            int len = s1.length() + s2.length();
            String s1s2 = s1 + s2;
            String s2s1 = s2 + s1;
            for(int i = 0; i < len; i++) {
                int p = s1s2.charAt(i) - '0', q = s2s1.charAt(i) - '0';
                if(p < q) return -1;
                else if (p > q) return 1;
            }
            return 0;
        }
    }
}