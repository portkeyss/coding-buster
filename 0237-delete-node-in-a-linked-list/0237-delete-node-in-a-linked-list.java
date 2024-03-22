/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) { val = x; }
 * }
 */
public class Solution {
    public void deleteNode(ListNode node) {
        ListNode t = node;
        ListNode pre = null;
        while(t.next != null) {
            t.val = t.next.val;
            pre = t;
            t = t.next;
        }
        pre.next = null;
    }
}