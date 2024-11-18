# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        group =k
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
        new_head = None
        for i in arr:
            for j in i:
                node = ListNode(j)
                if(len(i)==k):
                    node.next = new_head
                    new_head = node
            while(new_head):
                fin.next = new_head
                fin=fin.next
                new_head = new_head.next
        if(k!=1 and le%k!=0):
            for i in arr[-1]:
                fin.next = ListNode(i)
                fin = fin.next
        return ans.next