# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.maxi=0
        def help(root):
            
            if not root:
                return 0
            left = help(root.left)
            right = help(root.right)
            res = left+right
            if(self.maxi<res):
                self.maxi =res
            return max(left,right)+1
        help(root)
        return self.maxi


            
        