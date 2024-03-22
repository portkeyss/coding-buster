public class Solution {
    public int[] searchRange(int[] A, int target) {
        int[] range = new int[2];
        int start = 0;
        int end = A.length - 1;
        while (start <= end) {
            int mid = (start + end)/2;
            if (A[mid] < target) start = mid + 1;
            else if (A[mid] > target) end = mid - 1;
            else {
                int i = mid, j = mid;
                for (; i >= 0 && A[i] == target; i--);
                range[0] = i + 1;
                for (; j <= A.length -1 && A[j] == target; j++);
                range[1] = j - 1;  
                return range;
            }
        }
        range[0] = -1; range[1] = -1; return range;
    }
}