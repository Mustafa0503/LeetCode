class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        
        temp = []
        fin = []
        def helper(openC,closeC):
            
            if(openC==closeC==n):
                fin.append("".join(temp))
                return
            if(openC<n):
                temp.append('(')
                helper(openC+1,closeC)
                temp.pop()

            if(openC>closeC):
                temp.append(")")
                helper(openC,closeC+1)
                temp.pop()
          
        helper(0,0)
        return fin
            
