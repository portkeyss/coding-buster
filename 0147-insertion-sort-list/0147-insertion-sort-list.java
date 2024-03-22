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
    public ListNode insertionSortList(ListNode head) {
        if (head == null ||head.next == null) return head;
        
        ListNode p = head;
        ListNode q = head.next;
        
        ListNode pre = null;
        ListNode t = null;
        int count = 1;
        
        head.next = null;
        // it is crucial to ensure that the newly constructed list has an end; we construct the list from
        // the old list, each time creating a new node
        
        while ( q!= null ) {
            p = head;
            pre = null;
            while (p != null ) {
                if (p.val <= q.val ) {
                    pre = p;
                    p = p.next;
                 }
                else break;
            }
           
            if (pre == null) head = q;
            else pre.next = q;
        
            t = q.next;
            q.next = p;
            q = t;
         }
         return head;
     }      
}      
       