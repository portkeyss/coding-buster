/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */
class Solution {
public:
    ListNode* oddEvenList(ListNode* head) { 
        if(head == NULL) return NULL;
        if(head->next == NULL) return head;
        ListNode *even_head = head->next;
        ListNode *cur = head, *prev = NULL, *nxt= NULL;
        int i = 1;
        while(cur->next != NULL){
            nxt = cur->next;
            cur->next = nxt->next;
            prev = cur;
            cur = nxt;
            i++;
        }
        if(i%2 == 0) {
            prev->next = even_head;
        }else{
            cur->next = even_head;
        }
        return head;
    }
};