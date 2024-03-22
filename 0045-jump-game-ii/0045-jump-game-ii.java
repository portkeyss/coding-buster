public class Solution {
    public int jump(int[] A) {
        if(A.length == 1) return 0;
        int max = 0; 
        int step = 0; 
        int cur = 0; 
        while(max < A.length - 1) { 
            int nextMax = 0; 
            for(int i = cur; i <= max; i++) { 
                int temp = i + A[i]; 
                if(nextMax < temp) nextMax = temp; 
            }           
            if(nextMax == max) return -1;
            step++; 
            if(nextMax >= A.length -1) return step;
            cur = max + 1;     
            max = nextMax;       
        } 
        return -1; 
    }
}