public class Solution {
    public String convert(String s, int nRows) {
        if(nRows == 1) return s;
        StringBuffer[] sbs = new StringBuffer[nRows];
        for (int i = 0; i < nRows; i++) 
             sbs[i] = new StringBuffer();
        int j = 0;
        int k = nRows - 2;
        for (int i = 0; i < s.length(); i ++) {
            int m = i % (2 * nRows - 2);
            if(m < nRows) { sbs[j].append(s.charAt(i)); j = (j + 1) % nRows; }
            else {sbs[k].append(s.charAt(i)); k = nRows - 2 - (nRows - k -1) % (nRows - 2); }
        }
        for(int i = 1; i< nRows; i++)
           sbs[0].append(sbs[i]);
        return sbs[0].toString();
    }
}