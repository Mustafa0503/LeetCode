# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if(not head or head.next==None and n==1):
            return None
        f = head
        leng =0
        while(f!= None):
            f=f.next
            leng+=1
        target = leng-n
        if(target == 0):
            return head.next
        c=1
        f1 = head
        f2=f1.next

        while(f1.next!=None):
            if(c==target):
                f1.next = f2.next
                break
            f1=f1.next
            f2 = f2.next
            c+=1
        return head