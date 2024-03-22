/* The read4 API is defined in the parent class Reader4.
      int read4(char[] buf); */

public class Solution extends Reader4 {
    //do not misunderstand this problem. It requires one to write into the buffer from index 0 every time the funtion/method is called. This is actually simple because we do not need to trace the accumulative indices. from the client perspective, each time the function is called, the buf is read from 0 to the index equalling the returned integer value
    //the key difference between multiple calls and single call is that the previous call to read4 might sucked in more characters than needed for the previous visit, therefore the current call first need to check from the residual characters left from preceeding calls before one really call read4 again. we use a queue called residue to store the "overflow" characters for future calls
    
    LinkedList<Character> residue= new LinkedList<Character>();
    char[] buf4 = new char[4];
    /**
     * @param buf Destination buffer
     * @param n   Maximum number of characters to read
     * @return    The number of characters read
     */
    public int read(char[] buf, int n) {
        int cur = 0;
        int res_sz = residue.size();
        int poll_sz = Math.min(res_sz, n);
        for(int i = 0; i < poll_sz; i++) buf[i] = residue.pollFirst();
        cur += poll_sz;
        if(n <= res_sz) return n;
        while(true) {
            int m = read4(buf4);
            int len = Math.min(m, n - cur);// n - cur is the number of characters that need to be read after last call of read4
            for(int i = 0; i < len; i++) buf[i+cur] = buf4[i];
            if(n - cur < m) { //place characters that are read but not used into the residue queue
                for(int i = n - cur; i < m; i++) residue.addLast(buf4[i]);
            }
            cur += len;
            if(cur == n || m < 4) return cur;
        }
    }
}