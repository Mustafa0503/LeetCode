# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        head = ListNode(0)
        l3 = head
        if(len(lists)!=0):
            l1 = lists[0]
        else:
            return None
        for i in range(len(lists)-1):
            
            l2=lists[i+1]
            while(l1!=None and l2!=None):
                if(l1.val<=l2.val):
                    l3.next = ListNode(l1.val)
                    l3=l3.next
                    l1=l1.next
                elif(l1.val>l2.val):
                    l3.next = ListNode(l2.val)
                    l3=l3.next
                    l2=l2.next
            if(l1!=None):
                l3.next= l1
            if(l2!=None):
                l3.next= l2
            l3 = head
            l1=head.next
            yo = l1
            # while(yo):
            #     print(yo.val)
            #     yo = yo.next
            # print("********************************")
        return l1