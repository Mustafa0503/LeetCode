class Solution:
    def myAtoi(self, s: str) -> int:

        digitF=False
        spaceF=False
        negF=False
        leadZero=False
        posF=False
        res = ""
        for i in s:
            if(i==' '):
                if(spaceF==True and (digitF or leadZero or negF or posF)):
                    break
                spaceF=True
                continue
            elif(i=='-' or i=='+'):
                if(leadZero==True or negF or posF or digitF):
                    break
                negF=True
                if(i=='+'):
                    negF=False
                    posF=True
                continue
            elif(i.isdigit() and int(i)!=0):
                digitF=True
                res = res + i
            elif(i.isdigit() and int(i)==0 and not digitF):
                leadZero=True
                continue
            elif(not i.isdigit()):
                break
            else:
                res = res + i
        if(negF==True):
            if(res==""):
                return 0
            if(int(res)*-1<-2 ** 31):
                return -2 ** 31
            return int(res)*-1
        else:
            if(res==""):
                return 0
            if(int(res)>2**31 - 1):
                return 2**31 - 1
            return int(res)
            