public class Solution {
    public List<Integer> majorityElement(int[] nums) {
        List<Integer> res = new LinkedList<Integer>();
        int n = nums.length;
        int box1 = Integer.MAX_VALUE, box2 = Integer.MAX_VALUE, cnt1 = 0, cnt2 = 0;
        for(int i = 0; i < n; i++ ) {
            if(nums[i] == box1) cnt1++;
            else if(nums[i] == box2) cnt2++;
            else if(cnt1 == 0) {box1 = nums[i]; cnt1++;}
            else if(cnt2 == 0) {box2 = nums[i]; cnt2++;}
            else {cnt1--; cnt2--;}
        }
        cnt1 = 0;
        cnt2 = 0;
        for(int i = 0; i < n; i++) {
            if(nums[i] == box1) cnt1++;
            else if(nums[i] == box2) cnt2++;
        }
        if(cnt1 > n/3) res.add(box1);
        if(cnt2 > n/3) res.add(box2);
        return res;
    }
}