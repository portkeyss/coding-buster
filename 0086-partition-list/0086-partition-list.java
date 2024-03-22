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
    public ListNode partition(ListNode head, int x) {
        if (head == null || head.next == null ) return head;
        
        ListNode p = head;
        ListNode shead = null;
        ListNode ghead = null;
        ListNode s = null;
        ListNode g = null;
        
        while ( p!= null) {
            if (p.val < x) {
                if (s == null) {
                    shead = p;
                    s = p;
                }
                else {
                    s.next = p;
                    s = p;
                }
            }
            else {
                if(g == null) {
                    ghead = p;
                    g = p;
                }
                else {
                    g.next = p;
                    g = p;
                }
            }
            p = p.next;
        }
        if(shead == null) return ghead;
        else {
            s.next = ghead;
            if (g!= null) g.next = null;
            return shead;
        }
    }
}