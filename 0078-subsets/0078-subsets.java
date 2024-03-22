public class Solution {
    public List<List<Integer>> subsets(int[] S) {
        Arrays.sort(S);
        int len = S.length;
        List<List<Integer>> result = new ArrayList<List<Integer>>();
        subsets(S,0,result);
        return result;
    }
    private void subsets(int[] S, int start, List<List<Integer>> result) {
        if(start == S.length) {
            List<Integer> p = new ArrayList<Integer>();
            result.add(p);
            return;
        }
        subsets(S, start + 1, result);
        int originalSize = result.size();
        for(int i = 0; i < originalSize; i++){
           List<Integer> l = result.get(i);
           List<Integer> p = new ArrayList<Integer>();
           p.addAll(l);
           p.add(0,S[start]);
           result.add(p);
        }
    }
}