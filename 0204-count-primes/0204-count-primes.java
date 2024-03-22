public class Solution {
    public int countPrimes(int n) {
        boolean[] notPrime = new boolean[n];
        int m = (int) Math.sqrt((double) (n-1));
        for(int i = 2; i <= m; i++) {
            if(notPrime[i]) continue;
            int j = 0;
            while(true) {
                int k = i * i + j * i;
                if(k >= n) break;
                notPrime[k] = true;
                j++;
            }
        }
        int result = 0;
        for(int i = 2; i < n; i++) {
            if(!notPrime[i]) result++;
        }
        return result;
    }
}