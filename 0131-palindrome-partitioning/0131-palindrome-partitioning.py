class Solution:

    def partition(self, s: str) -> List[List[str]]:
        def palindrome(s):
            return s == s[::-1] 
        ans = []
        temp=[]
        def dfs(ind):
            print("temp: ",temp,"ind: ",ind)
            if ind == len(s):
                ans.append(temp.copy())
                return
            print("got here")
            for i in range(ind,len(s)):
                if(palindrome(s[ind:i+1])):
                    temp.append(s[ind:i+1])
                    dfs(i+1)
                    temp.pop()
        dfs(0)
        return ans