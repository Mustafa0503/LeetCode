# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if(not head):
            return False
        h = head
        while(h.next):
            if(h.next.val==-98):
                return True
            h.val = -98
            h=h.next
        return False