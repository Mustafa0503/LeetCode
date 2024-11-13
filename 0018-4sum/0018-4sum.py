class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        res = []
        for i in range(len(nums)):
            if(i!=0 and nums[i]==nums[i-1]):
                continue
            for j in range(i+1,len(nums)):
                # if(nums[j]==nums[j-1]):
                #     continue
                l=j+1
                r=len(nums)-1
                while(l<r):
                    summm =nums[i]+nums[j]+nums[l]+nums[r]
                    if(summm==target):
                        
                        ar = [nums[i],nums[j],nums[l],nums[r]]
                        ar.sort()
                        if(ar not in res):
                            res.append(ar)
                        l+=1
                        
                            
                    elif(summm>target):
                        r-=1
                    elif(summm<target):
                        l+=1
        return res