/* The read4 API is defined in the parent class Reader4.
      int read4(char[] buf); */

public class Solution extends Reader4 {
    /**
     * @param buf Destination buffer
     * @param n   Maximum number of characters to read
     * @return    The number of characters read
     */
    public int read(char[] buf, int n) {
        int cur = 0;
        char[] buf4 = new char[4];
        while(true) {
            int m = read4(buf4);
            int len = Math.min(m, n - cur);
            for(int i = 0; i < len; i++) buf[i+cur] = buf4[i];
            cur += len;
            if(cur == n || m < 4) return cur;
        }
    }
}