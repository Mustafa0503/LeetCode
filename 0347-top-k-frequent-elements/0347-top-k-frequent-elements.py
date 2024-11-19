class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d={}
        ans=[]
        fin=[]
        for i in nums:
            d[i] = 1+d.get(i,0)
        f = list(d.values())
        f.sort(reverse=True)
        i=0
        while(i<k):
            ans.append(f[i])
            i+=1
        for key in d:
            if(d[key] in ans):
                fin.append(key)
        return fin[:k]
