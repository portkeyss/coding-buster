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
    public ListNode sortList(ListNode head) {
        if(head == null || head.next == null) return head; 
        int n = 0; 
        for(ListNode l = head; l != null; l = l.next) n++; 
        for(int sz = 1; sz < n ; sz <<= 1) { 
            ListNode h = head; // h is the head of the sublist being analyzed
            ListNode t = null; // t is the tail of the sublist being analyzed
            while(h != null) { 
                ListNode l1 = h, l2 = h;
                int count = 0; 
                ListNode pre_l2 = null;
                while(l2 != null && count < sz) {pre_l2 = l2; l2 = l2.next; count++;} 
                if(l2 == null) {t.next = h; break;}
                else h = (l1.val <= l2.val) ? l1 : l2;
                
                if(t == null) head = h;
                else t.next = h;// t.next points to the new h
                
                pre_l2.next = null;//demarcate the correct bound for l1 sublist
                h = l2;
                ListNode pre_h = null;
                while(h != null && count < 2 * sz) {pre_h = h; h = h.next; count++;}
                if(h != null) pre_h.next = null;//demarcate the correct bound for l2 sublist
                 
                ListNode l = new ListNode(0);
                //the choice of value is arbitrary, l is the node before h and will iterate across the list
                l.next = h;
                while(l1 != null && l2 != null) {
                    if (l1.val <= l2.val) {l.next = l1; l1 = l1.next;}
                    else {l.next = l2; l2 = l2.next;}
                    l = l.next;
                }
                if(l1 == null) {l.next = l2; t = pre_h;}
                //find the right tail of this sublist to connect to next h waiting to be found in next loop
                else if(l2 == null) {l.next = l1; t = pre_l2;}
                //find the right tail of this sublist to connect to next h waiting to be found in next loop
            } 
        } 
        return head;
    }
}