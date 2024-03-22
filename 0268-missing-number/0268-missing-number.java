class Solution {
    public int missingNumber(int[] nums) {
        int n = nums.length;
        int expectedSum = (1 + n) * n / 2;
        int actualSum = 0;
        for(int i : nums){
            actualSum += i;
        }
        int missingValue = expectedSum - actualSum;
        return missingValue;
    }
}