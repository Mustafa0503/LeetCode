class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        hit = len(s)/2
        count=0
        op=["(","[","{"]
        if(len(s)==0):
            return True
        if(len(s)%2!=0):
            return False
        for i in s:
           
            if(i in op):
                
                stack.insert(0,i)
            else:
                
                if(len(stack)!=0):
                    if(stack[0]=="(" and i!=")" or stack[0]=="{" and i!="}" or stack[0]=="[" and i!="]"):
                        return False
                    print(count)
                    stack = stack[1:]
                    count+=1

        if(len(stack)==0 and hit==count):
            return True
        return False