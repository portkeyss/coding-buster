public class Solution {
    public List<List<Integer>> threeSum(int[] num) {
        Arrays.sort(num);
        int N = num.length;
        List<List<Integer>> result = new ArrayList<List<Integer>>();
        for(int i = 0; i < N - 2 && num[i] <= 0; i++) {
             if(i > 0 && num[i-1] == num[i]) continue;
             for(int j = i+1; j < N - 1; j++) {
                if(j > i+1 && num[j -1] == num[j]) continue;
                int temp = - num[i] - num[j];
                int index = findIndex(temp, num, j+1);
                if(index == -1) continue;
                List<Integer> l = new ArrayList<Integer>();
                l.add(num[i]); l.add(num[j]); l.add(num[index]);
                result.add(0,l);
            }
            }
        return result;
    }
    private int findIndex(int val, int[] num, int start) {
        int end = num.length - 1;
        while(start <= end) {
            int mid = (start + end)/2;
            if(num[mid] == val) return mid;
            else if (num[mid] < val) start = mid + 1;
            else end = mid - 1;
        }
        return -1;
    }
}