public class Solution {
    public int countDigitOne(int n) {
        if(n <= 0) return 0;
        int cnt = 0;
        int cntCeiling = 0;
        int k = 1;
        int m = 1;
        while(n > 0) {
            int d = n % 10;
            if(d == 1) cnt += cntCeiling + m;
            else if (d > 1) cnt += d * cntCeiling + k;
            cntCeiling = 10 * cntCeiling + k;
            m += d * k;
            k *= 10;
            n /= 10;
        }
        return cnt;
    }
}