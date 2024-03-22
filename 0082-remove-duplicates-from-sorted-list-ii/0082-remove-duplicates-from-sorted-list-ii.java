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
    public ListNode deleteDuplicates (ListNode head) {
        if(head == null || head.next == null) return head;
        ListNode p = head;
        ListNode q = null;
        ListNode pre = null;
        
        int dup = 0;
        
        while (p != null && p.next != null) {
            q = p.next;
            while (q != null && q.val == p.val) {
                q = q.next; 
                dup ++;
            }
            
            if (dup > 0)  {
                if (q == null) {
                 if (pre == null) head = null;
                 else pre.next = null;
                 return head;
                }
            else {
                    if(pre == null) head = q;
                    else pre.next = q;
                    dup = 0; 
                }
            }
            else {
                if (pre == null) head = p;
                else pre.next = p;
                pre = p;
            }
            p = q;
        }
        return head;
    }
}