# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.sol = []
        def help(root):
            if not root:
                return
            help(root.left)
            self.sol.append(root.val)
            help(root.right)
            return self.sol
        return help(root)[k-1]
            