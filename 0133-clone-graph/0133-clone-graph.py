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
        if node is None:
            return None
        hash_table = {}

        def dfs(node1):
            if node1 is None or node1 in hash_table:
                return
            new_node = Node(node1.val)
            hash_table[node1] = new_node
            for nbr in node1.neighbors:
                dfs(nbr)
        
        dfs(node)

        for node2 in hash_table:
            for nbr in node2.neighbors:
                hash_table[node2].neighbors.append(hash_table[nbr])

        return hash_table[node]