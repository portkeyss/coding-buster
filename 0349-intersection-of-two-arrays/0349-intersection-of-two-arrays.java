class Solution {
    public int[] intersection(int[] nums1, int[] nums2) {
        HashSet<Integer> numSet1 = new HashSet<Integer>();
        for(int num : nums1){
            numSet1.add(num);
        }
        HashSet<Integer> numSet2 = new HashSet<Integer>();
        for(int num : nums2){
            numSet2.add(num);
        }
        HashSet<Integer> numSet3 = new HashSet<Integer>();
        for(int num: numSet1){
            if(numSet2.contains(num)) numSet3.add(num);
        }
        int[] result = new int[numSet3.size()];
        int i = 0;
        for(int num: numSet3){
            result[i] = num;
            i++;
        }
        return result;
    }
}