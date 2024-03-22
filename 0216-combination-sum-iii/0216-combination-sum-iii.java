public class Solution {
    LinkedList<Integer> auxStack = new LinkedList<Integer>();
    List<List<Integer>> rslt = new LinkedList<List<Integer>>();
    public List<List<Integer>> combinationSum3(int k, int n) {
        combinationSum3(k, n, 0);
        return rslt;
    }
    private void combinationSum3(int k, int n,int lastNum) {
        if(k == 1) {
            if(n <= lastNum || n > 9) return;
            List<Integer> list = new LinkedList<Integer>();
            list.addAll(auxStack);
            list.add(n);
            rslt.add(list);
            return;
        }
        for(int i = lastNum + 1; i <= 9; i++) {
            auxStack.addLast(i);
            combinationSum3(k - 1, n - i, i);
            auxStack.pollLast();
        }
    }
}