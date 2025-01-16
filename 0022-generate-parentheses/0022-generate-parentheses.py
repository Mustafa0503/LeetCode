class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans = []
        l=0
        r=0
        t=[]
        def helper(l,r,t):
            if(l==r==n):
                ans.append("".join(t))
                return
            if(l<n):
                t.append("(")
                helper(l+1,r,t)
                t.pop()
            if(r<n and r<l):
                t.append(")")
                helper(l,r+1,t)
                t.pop()
        helper(l,r,t)
        return ans