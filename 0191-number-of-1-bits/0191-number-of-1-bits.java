public class Solution {
    // you need to treat n as an unsigned value
    public int hammingWeight(int n) {
        int result = 0;
        int mask = 1;
        for(int i = 0; i < 32; i++) {
            if((mask & n) == 1) result++;
            n >>>= 1;
        }
        return result;
    }
}