public class Solution {
    public String simplifyPath(String path) {
        String[] dir = path.split("/");
        StringBuffer sb = new StringBuffer();
        Deque<String> deque = new LinkedList<String>();
        for(String d: dir) {
            if(d.equals("" ) || d.equals(".")) continue;
            else if(d.equals("..")) {if(!deque.isEmpty()) deque.pollLast();} 
            else deque.offerLast(d); 
        }
        if(deque.isEmpty()) return "/";
        for(String d: deque) sb.append("/").append(d);
        return sb.toString();
    }
}