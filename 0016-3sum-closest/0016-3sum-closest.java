public class Solution {
    public int threeSumClosest(int[] num, int target) {
        Arrays.sort(num);
        int N = num.length;
        int closest = 1 << 30;//Just chose a very large number
        for(int i = 0; i < N - 2; i++) {
             if(i > 0 && num[i-1] == num[i]) continue;
             for(int j = i+1; j < N - 1; j++) {
                if(j > i+1 && num[j -1] == num[j]) continue;
                int temp = num[i] + num[j];
                int index = findClosest(target - temp, num, j+1);
                temp += num[index];
                if (target == temp) return target;
                if(Math.abs(temp - target) < Math.abs(closest - target)) closest = temp;
            }
            }
        return closest;
    }
    private int findClosest(int val, int[] num, int start) {
        int end = num.length - 1;
        if(end == start) return start;
        
        //The following two lines are unnecessary, but it might save some time
        // The advantage of this step, is that we can ensure that (star, end) pair inherited from beginning, respect
        // the condition num[start] < val < num[end]. We can see from the while-loop that this condition always holds
        // because, if we measure the mid value, if its value equals val, it returns. If not, either start or end fall on
        // this mid position, and its value (> or <) val. num[start] < val < num[end] Always holds.
        if(val <= num[start]) return start;
        else if(val >= num[end]) return end;
        
        while(start < end - 1) {
            int mid = (start + end)/2;
            if(num[mid] == val) return mid;
            else if (num[mid] < val) start = mid;
            else end = mid;
        }
        
       //If this point is reached, it means that start = end - 1;
       if(val - num[start] <= num[end] - val) return start; 
       // it was originally assummed that until this step num[start] < val < num[end]. This is correct if we retain the two
       // line code which I claim to be unnecessary. But if the two line code are commented out, the program still runs well.
       // But note that this does not mean num[start] <= val <= num[end] is always correct if we comment out the two line code
       // It is possible that val <= num[start] or val >= num[end]. But if we carefully observe that, the "if" statement still
       // make the correct selection.
       return end;
    }
}