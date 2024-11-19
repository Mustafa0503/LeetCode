# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        group =k
        new_head = None
        arr = []
        fin = ListNode(0)
        ans = fin
        one =[]
        while(head):
            if(head and group>0):
                one.append(head.val)
                group = group -1
                head = head.next
            else:
                group = k
                for p in reversed(one):
                    node = ListNode(p)
                    fin.next = node
                    fin = fin.next
                arr.append(one)
                one = []
        if(len(one) !=k):
            for p in (one):
                node = ListNode(p)
                fin.next = node
                fin = fin.next
        else:
            for p in reversed(one):
                node = ListNode(p)
                fin.next = node
                fin = fin.next
        return ans.next