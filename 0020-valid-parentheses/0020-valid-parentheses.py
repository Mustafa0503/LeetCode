class Solution:
    def isValid(self, s: str) -> bool:
        if(len(s)==0):
            return True
        if(len(s)%2!=0):
            return False
        stack = []
        hit = len(s)/2
        count=0
      
        mapping = {')': '(', '}': '{', ']': '['}
        for i in s:
            if(i not in mapping):
                stack.append(i)
            else:
                if(len(stack)!=0):
                    peek = stack.pop()
                    if(peek!=mapping[i]):
                        return False
                    
                    count+=1
        if(len(stack)==0 and hit==count):
            return True
        return False