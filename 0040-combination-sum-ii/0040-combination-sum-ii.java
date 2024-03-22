public class Solution {
    public List<List<Integer>> combinationSum2(int[] num, int target) {
        Arrays.sort(num);
        List<List<Integer>> result = new ArrayList<List<Integer>>();
        Deque<Integer> used = new LinkedList<Integer>();
        combinationSum2(num, target, 0, result, used);
        return result;
    }
    private void combinationSum2(int[] num, int target, int start, List<List<Integer>> result, Deque<Integer> used){ 
        int t = findIndex(num, target, start);
        if (t != -1 ) { 
            used.add(num[t]);
            List<Integer> p = new ArrayList<Integer>(); p.addAll(used); result.add(p);
            used.removeLast();
        }
        for(int i = start; i + 1 < num.length && target - num[i] >= num[i+1] ; i++) {
            if(i - 1 >= start && num[i] == num[i-1]) continue;
            used.add(num[i]); 
            combinationSum2(num,target - num[i], i + 1, result, used); 
            used.removeLast();
        }
    }
    private int findIndex(int[] num, int t, int start) {
        int end = num.length - 1;
        while(start <= end) {
            int mid = (start + end) /2; 
            if(num[mid] == t) return mid;
            else if (num[mid] < t) start = mid + 1;
            else  end = mid - 1;
        }
        return -1;
    }
}