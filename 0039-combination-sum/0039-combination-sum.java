public class Solution {
    public List<List<Integer>> combinationSum(int[] candidates, int target) {
        Arrays.sort(candidates);
        List<List<Integer>> result = new ArrayList<List<Integer>>();
        List<Integer> used = new ArrayList<Integer>();
        combinationSum(candidates, target, candidates.length - 1, result, used);
        return result;
    }
    private void combinationSum(int[] candidates, int target, int bound, List<List<Integer>> result, List<Integer> used){ 
        int t = findIndex(candidates, target, bound);
        if (t != -1 ) {
            used.add(0,candidates[t]);
            List<Integer> p = new ArrayList<Integer>(); p.addAll(used); result.add(p);
            used.remove(0);
        }
        for(int i = 0; i <= bound && target - candidates[i] >= candidates[0] ; i++) { 
            used.add(0,candidates[i]); 
            combinationSum(candidates,target - candidates[i], i, result, used); 
            used.remove(0);
        }
    }
    private int findIndex(int[] num, int t, int end) {
        int start = 0;
        while(start <= end) {
            int mid = (start + end) /2; 
            if(num[mid] == t) return mid;
            else if (num[mid] < t) start = mid + 1;
            else  end = mid - 1;
        }
        return -1;
    }
}