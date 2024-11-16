# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        if(not head): return head
        l1 = head
        fin  = ListNode(head.val)
        
        while(l1.next):
            new_node = ListNode(l1.next.val)
            new_node.next = fin
            fin =new_node 
            l1 = l1.next
        return fin
            