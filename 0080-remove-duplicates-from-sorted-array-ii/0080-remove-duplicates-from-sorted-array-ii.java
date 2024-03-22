public class Solution {
    public int removeDuplicates(int[] A) {
        int i = 0;
        int j = 0;
        int k = 0;
        
        while (i < A.length) {
            int count = 0;
            while (j < A.length) {      
                if(A[i] != A[j]) break;
                else if (count < 2) {
                    A[k++] = A[j++];
                    count ++;
                }
                else {
                    j++;
                    count++;
                    }
             }
             i = j;
        }
        return k;
    }
}