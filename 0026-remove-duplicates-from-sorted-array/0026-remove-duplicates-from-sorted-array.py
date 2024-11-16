class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        s= {}
        i=0
        while(i<len(nums)):
            if(nums[i] not in s):
                s[(nums[i])]=(nums[i])
                i+=1
            else:
                del nums[i]
        return len(nums)
     