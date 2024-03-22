public class Solution {
    // you need treat n as an unsigned value
    public int reverseBits(int n) {
       int m = 0;
       int mask = 1;
       for(int i = 0; i < 32; i++) {
           m <<= 1; 
           m |= mask & n; 
           n >>>= 1;
       }
       return m;
    }
}