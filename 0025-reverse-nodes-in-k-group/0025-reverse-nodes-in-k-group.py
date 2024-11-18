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
        le = 0
        while(head):
            one = []
            while(head and group>0):
                one.append(head.val)
                group = group -1
                head = head.next
                le+=1
            group = k
            arr.append(one)
            one = []
        for i in arr:
            for j in reversed(i):
                if(k==len(i)):
                    node = ListNode(j)
                    fin.next = node
                    fin = fin.next
        if(k!=1 and le%k!=0):
            for i in arr[-1]:
                fin.next = ListNode(i)
                fin = fin.next
        return ans.next