# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        group =k
        lhead = head
        arr = []
        last_head=None
        fin = ListNode(0)
        ans = fin
        le = 0
        while(lhead):
            one = []
            while(lhead and group>0):
                one.append(lhead.val)
                group = group -1
                lhead = lhead.next
                le+=1
            group = k
            arr.append(one)
            one = []
        for i in arr:
            new_head = last_head
            for j in i:
                node = ListNode(j)
                if(len(i)==k):
                    node.next = new_head
                    new_head = node
            last_head = new_head
            while(last_head):
                fin.next = last_head
                fin=fin.next
                last_head = last_head.next
        
        if(k!=1 and le%k!=0):
            for i in arr[-1]:
                fin.next = ListNode(i)
                fin = fin.next
        return ans.next