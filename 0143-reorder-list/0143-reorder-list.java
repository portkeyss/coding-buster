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
    public void reorderList(ListNode head) {
        // the basic idea is to reverse the second half of the list, then interweave the two half lists
        if (head == null || head.next == null || head.next.next == null) return;
        
        ListNode p = head;
        int length = 1; 
        while(p.next!= null){
            p =p.next;
            length++;
        }
        ListNode tail = p;
        
        //partition into two equal parts, [1 , length/2 ], [length/2+1 ,length], for both odd and even length
        p=head;
        int count = 1;
        while(count < length/2){
            p = p.next;
            count++;
        }
        
        ListNode mid = p.next;
        p.next = null;
        
        reverseList(mid, tail);
        interweave(head, tail);
    }
    private void reverseList (ListNode head, ListNode tail) {
    if (head == null) return;
    if (head == tail) return;
    
    ListNode pre = null;
    ListNode cur = head;
    ListNode post = null;
    
    while ( cur!= null){
        post = cur.next;
        cur.next = pre;
        pre = cur;
        cur = post;
    }
    }
    
    private void interweave (ListNode head1, ListNode head2) { 
    // this auxiliary method is applicable only for head1.length = head1.length, or head1.length = head2.length -1;
    // also, head1 goes first
        if(head1 == null) {
            head1 = head2;
            return;
        }
        if(head2 == null) return;
        ListNode p1 = head1;
        ListNode p2 = head2;
        ListNode pre = null;
       while(p1.next != null && p2 != null) { 
            ListNode q1 = p1.next;
            ListNode q2 = p2.next;
            p1.next = p2; 
            p2.next = q1; 
            p1 = q1; 
            p2 = q2; 
        } 
        p1.next = p2; 
    } 
}