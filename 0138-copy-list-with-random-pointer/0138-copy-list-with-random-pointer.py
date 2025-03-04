"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        temp = head
        new_list = Node(-1,None,None)
        track = new_list
        
        dic = {}
        while(temp):
            new_list.next = Node(temp.val,None,None)
            new_list = new_list.next
            dic[temp] = new_list
            temp = temp.next
        track = track.next
        fin = track
        while(head):
            if(head.random):
                track.random = dic[head.random]
            track = track.next
            head = head.next
        print(dic)
        return fin