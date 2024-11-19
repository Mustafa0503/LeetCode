class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if(len(s)!=len(t)):
            return False
        sl=list(s)
        tl=list(t)
        sl.sort()
        tl.sort()
        for i in range(len(s)):
            if(sl[i]!=tl[i]):
                return False
        return True
        