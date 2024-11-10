class Solution:
    def reverse(self, x: int) -> int:

        if(x==0):
            return 0
        fin=""
        nonZero=False
        neg = False
        if(x<0):
            neg = True
            num  = str(x*-1)
        else:
            num = str(x)
        for i in reversed(num):
            if(i!='0' or nonZero):
                fin = fin + i
                nonZero = True
        if(neg==True):
            if(int(fin)*-1<-2 ** 31 or int(fin)*-1>2**31 - 1):
                return 0
            return int(fin)*-1
        else:
            if(int(fin)<-2 ** 31 or int(fin)>2**31 - 1):
                return 0
            return int(fin)
       