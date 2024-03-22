public class Solution {
    public List<List<Integer>> combine(int n, int k) {
        if(n < k) return null;
        List<List<Integer>> result = new ArrayList<List<Integer>>();
        List<Integer> l = new ArrayList<Integer>();
        combine(n,k,result,l);
        return result;
    }
    private void combine(int n, int k, List<List<Integer>> result, List<Integer> l){
        if(l.size() == k) {
            result.add(l);
            return;
        }
        int i;
        if(l.size() == 0) i = 1;
        else i = l.get(l.size() - 1) + 1;
        for(; i <= n + l.size() - k + 1; i ++) {
           List<Integer> h = new ArrayList<Integer>();
           h.addAll(l);
           h.add(i);
           combine(n,k,result, h);
        }
    }
}