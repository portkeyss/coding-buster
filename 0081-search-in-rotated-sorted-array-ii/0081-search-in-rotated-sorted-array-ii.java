public class Solution {
    public boolean search(int[] A, int target) {
        int start = 0; 
        int end = A.length - 1;
        int min = findMinIndex(A);

        //note that start and end are indices that counts from min
        while (start <= end ) {
            int mid = (start + end) /2;
            if (A[(mid + min) % A.length] == target) return true;
            else if (A[(mid + min) % A.length] < target) start = mid + 1 ;
            else end = mid - 1;
        }
        return false;
    }
    public int findMinIndex(int[] A) {
        for (int i = 0; i < A.length -1; i ++) {
            if(A[i] > A[i + 1]) return i+1;
        }
        return 0;
    }
   /* public int findMinIndex(int[] A) {
        int L = 0, R = A.length - 1;
        while (L < R && A[L] >= A[R]) {
        int M = (L + R) / 2;
        if (A[M] > A[R]) {
            L = M + 1;
         } else if (A[M] < A[L]) {
           R = M;
         } else {   // A[L] == A[M] == A[R]
           L = L + 1;
         }
        }
        return L;
    }*/
}