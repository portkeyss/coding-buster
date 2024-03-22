public class Solution {
    public int maxProduct(int[] A) {
        /*this is a O(n) At least one pass and at most two pass algorithm. In fact, it might be easily simplied to one pass.
        one can evaluate in the intervals bounded either by  the natural bounds 0 and len - 1 or by zeros. in each                      interval, first traverse the entire interval and get a value
        if it is positive, then record this interval maximum. If it is negative, then we make a comparsion. from the start, we          iterate until we find the first negative product; from the end of the interval, iterate until we find the first negative         product. We then divide the interval product by the smaller of the two negative product. This is the interval maximum.
        proceed to the next one
        */
        int len = A.length;
        
        int max = A[0]; for(int i = 0; i < len; i++) if(A[i] >= 0) {max = A[i]; break;}
        //Note that since we use zeros to partition intervals, it is easy to forget zero might
        //also be the max product. So this step is to find the whether a nonnegative entry exists, if exist, make it max.This is         // to fix the bug that zero does not participate in the comparision in our approach.
        
        int i = 0; 
        while(i < len) {
            if(A[i] == 0) {i++; continue;}
            int prod = 1; int j = i;
            for(; j < len && A[j] != 0; j++) prod *= A[j];
            if(j > i+1 && prod < 0) {
                int prod1 = 1;
                for(int k = i; k < len && prod1 > 0; k++) prod1 *= A[k];
                int prod2 = 1;
                for(int l = j - 1; l > -1 && prod2 > 0; l--) prod2 *= A[l];
                if(prod1 > prod2) prod /= prod1; //note that because both prod1 and prod2 are negative, Abs(prod1) < Abs(prod2)
                else prod /= prod2;
            }
            if(prod > max) max = prod;
            i = j;
        }
        return max;
    }
}