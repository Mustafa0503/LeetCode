# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        if not root:
            return 0
        maxi = root.val
        self.goodNode = 0
        
        def dfs(self, root, maxi):
            print("maxi", maxi)
            if root==None:
                return
            print("val",root.val)
            
            if root.val>=maxi:
                self.goodNode+=1
                maxi = root.val
            print("goodnode", self.goodNode)
            dfs(self, root.left, maxi)
            dfs(self, root.right, maxi)
            return self.goodNode
        return dfs(self, root, maxi)
