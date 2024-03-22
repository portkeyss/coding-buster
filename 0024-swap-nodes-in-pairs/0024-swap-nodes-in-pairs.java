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
    public ListNode swapPairs(ListNode head) {
        if ( head == null || head.next == null) return head;
        ListNode newhead = head.next;
        ListNode h = head;
        ListNode temp = h;
    while (h != null && h.next != null){
            ListNode oldtemp = temp;
            temp = h;
            h = h.next;
            oldtemp.next = h;
            temp.next = h.next;
            h.next = temp;
            h = temp.next;
        }
        return newhead;
    }
}