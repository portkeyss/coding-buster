import java.lang.Integer;
public class Solution {
    public static int evalRPN(String[] tokens) {
        Stack<Integer> st = new Stack<Integer>();
        for(int i = 0; i < tokens.length; i++) {
            if(tokens[i].equals("+") || tokens[i].equals("-") || tokens[i].equals("*") || tokens[i].equals("/")) {
                int y = st.pop();
                int x = st.pop();
                if(tokens[i].equals("+"))  x += y;
                else if(tokens[i].equals("-") )  x -= y;
                else if(tokens[i].equals("*"))   x *= y;
                else if(tokens[i].equals("/"))  x /= y;
                st.push(x);
            }
            else {
                int j = Integer.parseInt(tokens[i]);
                st.push(j);
            }
        }
        return st.pop();
    }
}