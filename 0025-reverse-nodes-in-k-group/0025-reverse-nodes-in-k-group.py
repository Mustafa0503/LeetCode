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
                arr.append(one)
                one = []
        arr.append(one)
        one = []
        for i in arr:
            if(k==len(i)):
                for j in reversed(i):
                    node = ListNode(j)
                    fin.next = node
                    fin = fin.next
            else:
                for j in (i):
                    node = ListNode(j)
                    fin.next = node
                    fin = fin.next
        return ans.next