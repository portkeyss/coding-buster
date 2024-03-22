public class Solution {
    public List<List<Integer>> permute(int[] num) {
        Arrays.sort(num);
        List<List<Integer>> result = new ArrayList<List<Integer>>();
        List<Integer> used = new ArrayList<Integer>();
        permute(num,result,used);
        return result;
    }
    private void permute(int[] num, List<List<Integer>> result, List<Integer> used) {
        if(used.size() == num.length) {
            List<Integer> p = new ArrayList<Integer>();
            p.addAll(used);
            result.add(p);
            return;
        }
        for (int i = 0; i < num.length; i++ ) {
            if (used.contains(num[i])) continue;
            used.add(num[i]);
            permute(num, result, used);
            used.remove(used.size() -1);
        }
    }
}