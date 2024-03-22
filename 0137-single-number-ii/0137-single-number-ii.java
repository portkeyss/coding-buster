public class Solution {
    public int singleNumber(int[] A) {
        int ones = 0, twos = 0, threes = ~0;
        for(int i = 0; i < A.length; i++) {
            //if the number at a bit is zero, do nothing, else rotate one two three
            int previousOnes = ones;
            ones = ~A[i] & ones | A[i] & threes;
            int previousTwos = twos;
            twos = ~A[i] & twos | A[i] & previousOnes;
            threes = ~A[i] & threes | A[i] & previousTwos;
        }
        return ones;
    }
}