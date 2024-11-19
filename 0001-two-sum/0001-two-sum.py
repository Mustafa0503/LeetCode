class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        d={}

        for i in range(len(nums)):
            tar =(target - nums[i])
            if(d.get(tar)!=None):
                return [i, d[tar]]
            else:
                d[nums[i]] = i
        return -1