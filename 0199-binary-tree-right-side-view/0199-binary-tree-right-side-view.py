# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        sol = []
        sol.append([root.val])
        s1 = []
        s1.append(root)
        while s1:
            
            temp =[]
            tempSol = []
            for i in s1:
                if i.left:
                    temp.append(i.left)
                    tempSol.append(i.left.val)
                if i.right:
                    temp.append(i.right)
                    tempSol.append(i.right.val)
            s1 = temp
            if(tempSol):
                sol.append(tempSol)
        actulsol = []
        for i in sol:
            actulsol.append(i[-1])
        return actulsol
