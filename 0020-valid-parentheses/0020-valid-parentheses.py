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
                stack.insert(0,i)
            else:
                if(len(stack)!=0):
                    if(stack[0]!=mapping[i]):
                        return False
                    stack = stack[1:]
                    count+=1
        if(len(stack)==0 and hit==count):
            return True
        return False