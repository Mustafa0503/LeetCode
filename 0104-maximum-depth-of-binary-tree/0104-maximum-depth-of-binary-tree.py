# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        stack = []
        m=0
        if root == None:
            return 0
        stack.append(root.left)
        stack.append(root.right)
        a=0
        while stack:
            i=stack.pop()
            a = 1 + self.maxDepth(i)
            if a > m:
                m=a
            a=0
        return m
        