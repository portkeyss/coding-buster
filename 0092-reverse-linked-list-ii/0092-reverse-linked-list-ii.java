/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) {
 *         val = x;
 *         next = null;
 *     }
 * }
 */
public class Solution {
    public ListNode reverseBetween(ListNode head, int m, int n) {
        if (head == null || m >= n) return head;
        
        int count = 1;
        
        ListNode p = head;
        ListNode s = null;// the position before m; it is initialized to be null,which agrees with m == 1 case;
        ListNode pre = null;
        ListNode post = null;
        
       
        // To find the position for (m-1)th element. Note that it is only good for m>1.the case for m=1 should be treated               // differently 
       if (m > 1){
            while(count < m-1) {
               p = p.next;
               count ++;
            }   
            
            s=p;// the position before m
            
        // shift one step foward to reach m'th position
           p = p.next;
           count ++;
       }  
       
      
        while(count <= n) {
            post = p.next;
            p.next = pre;
            pre = p;
            p = post;
            count++;
        }
        
        if( m >1){
             ListNode q = s.next;
             s.next = pre;
             q.next = p;
        }
        else {
             ListNode q = head;
             head = pre;
             q.next = p;
        }
        return head;
    }
}