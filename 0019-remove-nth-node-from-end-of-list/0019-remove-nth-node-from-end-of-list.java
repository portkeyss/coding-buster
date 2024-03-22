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
    public ListNode removeNthFromEnd(ListNode head, int n) {
       if (head == null || n == 0 ) return head;
       
       ListNode p = head;
       ListNode q = p;
       int count = 0;
       while( count < n-1 && q != null){
           q = q.next;
           count ++;
       }
       if ( count == n-1 && q.next == null)  return head.next;
       if ( count < n-1 ) return head;
       
       while(q.next.next != null){
           p = p.next;
        q = q.next;
       }
       p.next = p.next.next;
       return head;
        
    }
}