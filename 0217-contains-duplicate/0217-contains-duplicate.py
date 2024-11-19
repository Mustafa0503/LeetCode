class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        d=set()
        for i in range(len(nums)):
            if(nums[i] in d):
                return True
            else:
                d.add(nums[i])
        return False