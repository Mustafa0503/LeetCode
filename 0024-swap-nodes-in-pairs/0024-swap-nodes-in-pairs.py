# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        #MOST DISGUSTING CODE THAT I'VE EVER WRTITEN IN MY ENTIRE LIFE HOLYYYY
        d = head
        c=0
        while(d):
            c=c+1
            d=d.next
        if(not head or head.next==None): return head
        elif(c==3):
            n1 = ListNode(head.next.val)
            n2 = ListNode(head.val)
            n1.next = n2
            n2.next = head.next.next
            return n1
        dum = ListNode(0,head)
        fin = head.next
        l1 = head
        l2 = head.next
        prev = None
        while(l1.next):
            if(prev): prev.next = l2
            temp = l2.next
            l2.next = l1
            l1.next = temp
            if(not l1.next): break
            prev = l1
            l1=l1.next
            l2=l1.next
            
        return fin