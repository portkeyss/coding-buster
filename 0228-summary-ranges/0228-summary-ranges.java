public class Solution {
    public List<String> summaryRanges(int[] nums) {
        List<String> result = new LinkedList<String>();
        if(nums.length == 0) return result;
        StringBuilder sb = new StringBuilder();
        sb.append(nums[0]);
        int pre = nums[0];
        boolean isStart = true;
        for(int i = 1; i < nums.length; i++) {
            if(pre != nums[i] - 1) {
                if(!isStart) sb.append(pre);
                result.add(sb.toString());
                sb.setLength(0);sb.append(nums[i]); isStart = true;
            }
            else if(isStart) {sb.append('-').append('>');isStart = false;}
            pre = nums[i];
        }
        if(!isStart) sb.append(pre);
        result.add(sb.toString());
        return result;
    }
}