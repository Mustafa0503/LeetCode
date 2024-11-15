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
        l1 = head
        l2=head.next
        l3 = ListNode()
        l4=l3
        l4.next = ListNode(l2.val)
        l4=l4.next
        l4.next = ListNode(l1.val)
        l4=l4.next
        while(l1.next and l1.next.next and l1.next.next.next):

            l1=l1.next.next
            l2=l1.next
            l4.next = ListNode(l2.val)
            l4=l4.next
            l4.next = ListNode(l1.val)
            l4=l4.next
        if(c%2!=0):
            l4.next = l1.next.next
        return l3.next