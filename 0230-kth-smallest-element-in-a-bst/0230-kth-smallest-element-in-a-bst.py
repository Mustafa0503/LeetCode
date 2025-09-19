# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        que = k*[0]
        self.sol = []
        def help(root):
            if not root:
                return
            self.sol.append(root.val)
            help(root.left)
            help(root.right)
            self.sol.sort()
            return self.sol
        ans = help(root)
        return ans[k-1]
            