class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d={}
        ans=[]
        a=[]
        fin=[[]for i in range(len(nums)+1)]
        for i in nums:
            d[i] = 1+d.get(i,0)
        for key in d:
            fin[d[key]].append(key)
        siz = 0
        o=1
        while(siz<k):
            if(fin[len(fin)-o]):
                for i in fin[len(fin)-o]:
                    if(siz<k):
                        ans.append(i)
                        siz+=1
            o+=1   
        
        return ans