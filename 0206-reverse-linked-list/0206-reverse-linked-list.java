/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) { val = x; }
 * }
 */
public class Solution {
    public ListNode reverseList(ListNode head) {//wrapper function consider the 0th case where the first part is null and 2nd part is the whole list
        if(head == null || head.next == null) return head;
        ListNode q = reverse(head);
        head.next = null;
        return q;
    }
    private ListNode reverse(ListNode head) {
        if(head == null || head.next == null) return head;
        ListNode p = head.next;
        ListNode q = reverse(p);
        p.next = head;
        return q;
    }
}