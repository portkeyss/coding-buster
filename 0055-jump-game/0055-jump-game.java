public class Solution {
    public boolean canJump(int[] A) {
        int max = 0;
        for(int i = 0; i < A.length && i <= max; i++) {
            int temp = i + A[i];
            if(temp > max) max = temp;
            if(max >= A.length -1)  return true;
        }
         return false;
    }
}