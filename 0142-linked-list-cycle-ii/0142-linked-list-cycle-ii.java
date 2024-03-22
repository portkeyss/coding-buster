/**
 * Definition for singly-linked list.
 * class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) {
 *         val = x;
 *         next = null;
 *     }
 * }
 */
public class Solution {
    public ListNode detectCycle(ListNode head) {
        if (head == null) return head;
        if (head.next == head) return head;
        
        ListNode p = head;
        ListNode q = head;
        
        while (p!= null && q != null && p.next != null && q.next != null && q.next.next != null){
            p = p.next;
            q = q.next.next;
            if (p == q ) break;
        }
        
        if (p == null || q == null || p.next == null || q.next == null || q.next.next == null) return null;
        else {
         q = head;
         while ( p != q) {
             p = p.next;
             q = q.next;
         }
         return p;
        }
    }
}