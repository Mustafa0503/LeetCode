# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        l1=list1
        l2=list2
        head = ListNode(0)
        l3 = head
        while(l1!=None and l2!=None):
            if(l1.val<l2.val):
                l3.next = ListNode(l1.val)
                l3=l3.next
                l1=l1.next
            elif(l1.val==l2.val):
                l3.next = ListNode(l1.val)
                l3=l3.next
                l3.next = ListNode(l2.val)
                l3=l3.next
                l1=l1.next
                l2=l2.next
            elif(l1.val>l2.val):
                l3.next = ListNode(l2.val)
                l3=l3.next
                l2=l2.next
        if(l1!=None):
            l3.next= l1
            
        if(l2!=None):
            l3.next= l2
        return head.next
