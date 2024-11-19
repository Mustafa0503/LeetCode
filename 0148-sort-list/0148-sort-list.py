# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        temp = []

        while(head):
            temp.append(head.val)
            head = head.next
        temp.sort()
        dum = ListNode(0)
        fin = dum
        for i in temp:
            dum.next = ListNode(i)
            dum = dum.next
        return fin.next
