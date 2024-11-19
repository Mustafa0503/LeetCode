class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if(len(s)!=len(t)):
            return False
        sd={}
        td={}
        for i in range(len(t)):
            sd[s[i]]=1+sd.get(s[i],0)  #.get return corresp val if dont exist then 0
            td[t[i]]=1+td.get(t[i],0)

        return sd==td
            

        


        