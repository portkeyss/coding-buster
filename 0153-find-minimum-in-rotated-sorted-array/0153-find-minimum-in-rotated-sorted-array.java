public class Solution {
    public int findMin(int[] num) {
        int start = 0;
        int end = num.length - 1;
        if (end == 0) return num[0];
        
        while (start < end && num[start] > num[end]){
            int mid = (start + end)/2;
            if (start == end - 1) {
                if (num[start] > num[end]) return num[end];
                else break;
            }
            else if (num[start] < num[mid]) start = mid;
            else if (num[mid] < num[end]) end = mid;
        }
        return num[0];
    }
}