class Solution {
    public int[] singleNumber(int[] nums) {
        int a = 0;
        for(int num: nums) a ^= num;
        a &= -a;
        int[] result = new int[2];
        for(int num: nums){
            if((num & a) == 0) result[0] ^= num;
            else result[1] ^= num;
        }
        return result;
    }
}