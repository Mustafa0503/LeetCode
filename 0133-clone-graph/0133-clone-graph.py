"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None
        dic = {node:Node(node.val)}
        q = deque([node])
        while(q):
            temp = q.popleft()

            for i in temp.neighbors:
                if i not in dic:
                    dic[i]=Node(i.val)
                    q.append(i)
                dic[temp].neighbors.append(dic[i])
        return dic[node]