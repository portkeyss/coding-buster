public class Solution {
    public boolean containsNearbyAlmostDuplicate(int[] nums, int k, int t) {
        int len = nums.length;
        TreeMap<Integer,Integer> tm = new TreeMap<Integer,Integer>();
        for(int i = 1; i < len && i <= k; i++) {
            if(nums[i] >= nums[0] - t && nums[i] <= nums[0] + t) return true;
            if(tm.containsKey(nums[i])) tm.put(nums[i],tm.get(nums[i]) + 1);
            else tm.put(nums[i],1);
        }
        for(int i = 1; i < len - 1; i++) {
            if(i + k < len) {
                if(tm.containsKey(nums[i+k])) tm.put(nums[i+k],tm.get(nums[i+k]) + 1);
                else tm.put(nums[i+k],1);
            }
            if(tm.get(nums[i]) == 1) tm.remove(nums[i]);
            else tm.put(nums[i],tm.get(nums[i]) - 1);
            Integer ceiling = tm.ceilingKey(nums[i] - t);
            if(ceiling != null && ceiling <= nums[i] + t) return true;
            Integer floor = tm.floorKey(nums[i] + t);
            if(floor != null && floor >= nums[i] - t) return true;
        }
        return false;
    }
}