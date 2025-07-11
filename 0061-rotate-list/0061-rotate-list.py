# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head:
            return head
        c = 0
        temp = head
        while temp:
            temp = temp.next
            c+=1
        k = k%c
        temp = head
        for _ in range(c-k-1):
            temp = temp.next
        head1 = temp.next
        temp.next = None
        if not head1:
            return head
        d = head1
        while d.next:
            d = d.next
        d.next = head
        return head1