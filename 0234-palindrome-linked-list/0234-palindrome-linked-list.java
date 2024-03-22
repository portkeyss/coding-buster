/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) { val = x; }
 * }
 */
public class Solution {
    public boolean isPalindrome(ListNode head) {
        int num = 0;
        ListNode h = head;
        while(h != null) {num++; h = h.next;}
        if(num < 2) return true;
        int i = 0;
        ListNode l = head;
        while(i < num / 2 - 1) {
            l = l.next; i++;
        }
        ListNode h2 = l.next;
        if(num % 2 == 0) l.next = null;
        ListNode tail = reverse(h2);
        return isEqual(head, tail);
    }
    private ListNode reverse(ListNode head) {
        ListNode pre = null, cur = head;
        while(cur != null) {
            ListNode nxt = cur.next;
            cur.next = pre;
            pre = cur;
            cur = nxt;
        }
        return pre;
    }
    private boolean isEqual(ListNode h1, ListNode h2) {
       while(h1 != null && h1.val == h2.val) {
           h1 = h1.next; h2 = h2.next;
       }
       return h1 == null;
    }
}