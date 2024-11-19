class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        d={}
        for i in range(len(nums)):
            if(nums[i] not in d):
                d[nums[i]]=i
            else:
                return True
        return False