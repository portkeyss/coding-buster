public class Solution {
    public int minSubArrayLen(int s, int[] nums) {
        int len = nums.length;
        if(len == 0) return 0;
        int[] sums = new int[len + 1];
        sums[0] = 0;
        for(int i = 1; i < len + 1; i++) sums[i] = sums[i-1] + nums[i - 1];
        int minLen = len + 1;//any number larger than the array length is fine
        for(int i = 0; i < len; i++) {
            int temp = findMinLen(sums[i] + s, sums,i);//note that sums[i] sums until i - 1; s defines the mininally required array summation of nums array from index i to smallest possible ending index. Therefore sums[i] + s should be smallest possible value in sums array that corresponds to nums array indexed from i to the smallest possible ending index
            minLen = Math.min(minLen, temp);
        }
        return minLen > len? 0 : minLen;
    }
    private int findMinLen(int val, int[] sums, int ss) {//ss is the smallest index for evaluation
        int start = ss, end = sums.length - 1;
        while(start <= end) {
            int mid = (start + end)/2;
            if(sums[mid] == val) return mid - ss;
            else if(sums[mid] < val) start = mid + 1;
            else if(sums[mid] > val) {
                if(mid == 0 || (mid - 1 >= 0 && sums[mid - 1] < val)) return mid - ss;
                else end = mid - 1;
            }
        }
        return sums.length + 1;
    }
}