class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if(len(s1)>len(s2)):
            return False
        def helper(d1,d2):
            for i in d1:
                if(i not in d2):
                    return False
                else:
                    if(d2[i]!=d1[i]):
                        return False
            return True
        d = {}
        d2={}
        ct = 0
        for i in s1:
            if(s2[ct] in d2):
                d2[s2[ct]]+=1
            else:
                d2[s2[ct]]=1
            ct+=1
            if (i in d):
                d[i]+=1
            else:
                d[i]=1
        ptr = 0
        if(helper(d,d2)):
            return True
        for i in range(len(s1),len(s2)):
            d2[s2[ptr]]-=1
            ptr+=1
            if(s2[i]in d2):
                d2[s2[i]]+=1
            else:
                d2[s2[i]]=1
            if(helper(d,d2)):
                return True
            
        return False