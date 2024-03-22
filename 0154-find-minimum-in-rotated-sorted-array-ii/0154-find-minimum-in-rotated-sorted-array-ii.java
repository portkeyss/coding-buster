public class Solution {
    public int findMin(int[] num) {
        return findMin(num, 0, num.length - 1);
    }
     private int findMin(int[] num, int start, int end) {
         if (start == end || num[start] < num[end]) return num[start];
         if (start == end - 1) return num[start] < num[end] ? num[start] : num[end];
         int mid = (start + end)/2;
         return findMin(num, start, mid) < findMin(num, mid+1, end)?findMin(num, start, mid) : findMin(num, mid+1, end);
     }
}