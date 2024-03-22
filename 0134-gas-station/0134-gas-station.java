public class Solution {
    public int canCompleteCircuit(int[] gas, int[] cost) {
        int N = gas.length;
        int i = 0;
        while (i < N) {
            if(gas[i] < cost[i]) {i++; continue;}

            int volume = 0;
            boolean reachUpperBound = false;
            int j = i;
            do {
                volume += gas[j] - cost[j];
                
                //This is to ensure we do not have to evaluate the starting point for duplicate times
                if(j == N-1 && !reachUpperBound) reachUpperBound = true;
                
                if(volume < 0) break;
                j = (j + 1) % N;
            } while(j != i );
            if (j == i) return i;
            if(reachUpperBound == true) return -1;
            i = j + 1;
        }
        return -1;
    }
}