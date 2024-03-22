public class Solution {
    public int rob(int[] nums) {
        // The idea is to make 2 iterations, the first one from 0 to nextlast number, the other one from 1 to last
        int previousTwo = 0, previousOne = 0, max1 = 0;
        int len = nums.length;
        if(len == 0) return 0;
        if(len == 1) return nums[0];//This corner case is easily forgetten
        for(int i = 0; i < len - 1; i++) {
            max1 = Math.max(previousOne, previousTwo + nums[i]);
            previousTwo = previousOne;
            previousOne = max1;
        }
        int max2 = 0;
        previousOne = 0; previousTwo = 0;
        for(int i = 1; i < len; i++) {
            max2 = Math.max(previousOne, previousTwo + nums[i]);
            previousTwo = previousOne;
            previousOne = max2;
        }
        return Math.max(max1,max2);
    }
}