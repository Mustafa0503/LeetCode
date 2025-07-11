class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        nums.sort()
        for n, i in enumerate(nums):
            if n!= i:
                return n
        return len(nums)