class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if(nums==[]):
            return 0
        if(len(nums)==1):
            return 1
        nums.sort()
        maxi = 0
        temp = 1
        for i in range(1, len(nums)):
            if(nums[i]==nums[i-1]+1):
                temp+=1
            elif(nums[i]==nums[i-1]):
                continue
            else:
                maxi = max(maxi,temp)
                temp=1
        maxi = max(maxi,temp)
        return maxi