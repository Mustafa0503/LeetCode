# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        self.t = True
        def help(root):

            if not root:
                return 0
            left_d = help(root.left)
            right_d = help(root.right)
            if(abs(left_d-right_d)>1):
                self.t = False
            return 1+max(left_d,right_d)
        help(root)
        return self.t
