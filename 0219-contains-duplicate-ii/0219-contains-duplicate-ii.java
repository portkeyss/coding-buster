public class Solution {
    public boolean containsNearbyDuplicate(int[] nums, int k) {
        HashMap<Integer,Integer> hm = new HashMap<Integer,Integer>();
        for(int i = 0; i < nums.length; i++) {
            if(hm.containsKey(nums[i]) && (hm.get(nums[i]) + k >= i)) return true;
            else hm.put(nums[i],i);
        }
        return false;
    }
}