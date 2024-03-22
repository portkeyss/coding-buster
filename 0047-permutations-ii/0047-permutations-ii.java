public class Solution {
    public List<List<Integer>> permuteUnique(int[] num) {
        Arrays.sort(num);
        List<List<Integer>> result = new ArrayList<List<Integer>>();
        List<Integer> used = new ArrayList<Integer>();
        List<Integer> usedIndices = new ArrayList<Integer>();
        permuteUnique(num,result,used,usedIndices);
        return result;
    }
    private void permuteUnique(int[] num, List<List<Integer>> result, List<Integer> used,List<Integer> usedIndices) {
        if(used.size() == num.length) {
            List<Integer> p = new ArrayList<Integer>();
            p.addAll(used);
            result.add(p);
            return;
        }
        for (int i = 0; i < num.length; i++ ) {
            if (usedIndices.contains(i) ||  (i > 0 && num[i] == num[i-1] && !usedIndices.contains(i-1))) continue;
            used.add(num[i]);
            usedIndices.add(i);
            permuteUnique(num, result, used, usedIndices);
            used.remove(used.size() -1);
            usedIndices.remove(usedIndices.size() -1);
        }
    }
}