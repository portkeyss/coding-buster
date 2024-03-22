public class Solution {
    public int rob(int[] num) {
        int len = num.length;
        int max = 0;
        int previousTwo = 0, previousOne = 0;
        for(int i = 0; i < len; i++) {
            max = Math.max(previousTwo + num[i], previousOne);
            previousTwo = previousOne;
            previousOne = max;
        }
        return max;
    }
}