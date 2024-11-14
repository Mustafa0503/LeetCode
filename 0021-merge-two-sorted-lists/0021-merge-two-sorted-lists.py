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
        if(l1==None):
            return l2
        if(l2==None):
            return l1
        while(l1!=None and l2!=None):
            print(l1.val,l2.val)
            print(l1.val==l2.val)
            if(l1.val<l2.val):
                print("no")
                l3.next = ListNode(l1.val)
                l3=l3.next
                l1=l1.next
            elif(l1.val==l2.val):
                print("what")
                l3.next = ListNode(l1.val)
                l3=l3.next
                l3.next = ListNode(l2.val)
                l3=l3.next
                l1=l1.next
                l2=l2.next
            elif(l1.val>l2.val):
                print("yop")
                l3.next = ListNode(l2.val)
                l3=l3.next
                l2=l2.next
        
        if(l1!=None):
            print("yp")
            l3.next= l1
            l3=l3.next
        if(l2!=None):
            print("tt")
            l3.next= l2
        return head.next
