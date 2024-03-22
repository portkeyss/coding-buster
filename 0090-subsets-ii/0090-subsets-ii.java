public class Solution {
    public List<List<Integer>> subsetsWithDup(int[] num) {
        Arrays.sort(num);
        int len = num.length;
        List<List<Integer>> result = new ArrayList<List<Integer>>();
        subsetsWithDup(num, 0, result);
        return result;
    }
    private void subsetsWithDup(int[] num, int start, List<List<Integer>> result) {
        if(start == num.length) {
            List<Integer> p = new ArrayList<Integer>();
            result.add(p);
            return;
        }
        int dup = 0;
        int val = num[start];
        while(start + dup < num.length && num[start + dup] == val) dup++;
        subsetsWithDup(num, start + dup,result);
        int originalSize = result.size();
        int s = 0;
        for(int d = 0; d < dup; d ++) {
            int i = s;
            for(; i < s + originalSize; i++){
               List<Integer> l = result.get(i);
               List<Integer> p = new ArrayList<Integer>();
               p.addAll(l);
               p.add(0,num[start]);
               result.add(p);
            }
            s = i;
        }
    }
}