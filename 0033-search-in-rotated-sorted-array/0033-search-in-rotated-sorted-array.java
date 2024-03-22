public class Solution {
    public int search(int[] A, int target) {
        int start = 0; 
        int end = A.length - 1;
        int min = findminindex(A);

        //note that start and end are indices that counts from min
        while (start <= end ) {
            int mid = (start + end) /2;
            if (A[(mid + min) % A.length] == target) return (mid + min) % A.length;
            else if (A[(mid + min) % A.length] < target) start = mid + 1 ;
            else end = mid - 1;
        }
        return -1;
    }
    private int findminindex (int[] A) {
        int start = 0;
        int end = A.length - 1;
        
        while (A[start] > A[end]){
            int mid = (start + end)/2;
            if (A[start] <= A[mid]) start = mid + 1;
            else if (A[mid] < A[end]) end = mid;
        }
        return start;
    }
}