class Solution {
    public boolean isMonotonic(int[] A) {
        int prev = A[0];
        int status = 0;
        int i = 1;
        for(; i < A.length; i++){
            if(A[i] == A[i-1]) continue;
            if(A[i] > A[i-1]) {
                status = 1;
                break;
            }else{
                status = -1;
                break;
            }
        }
        for(; i < A.length; i++){
            if(A[i] == A[i-1]) continue;
            if(A[i] > A[i-1]) {
                if(status == 1) continue;
                else return false;
            }else{
                if(status == -1) continue;
                else return false;
            }
        }
        return true;
    }
}