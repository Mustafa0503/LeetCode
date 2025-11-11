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

        q = deque([node])
        clone = {node: Node(node.val)}  

        while q:
            cur = q.popleft()
            for nei in cur.neighbors:
                if nei not in clone:
                    clone[nei] = Node(nei.val)
                    q.append(nei)
                clone[cur].neighbors.append(clone[nei]) 

        return clone[node]