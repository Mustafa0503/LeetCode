class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [0] * len(nums)
       
        pre = {}
        prefix = 1
        pre[0]=1
        for i in range(1,len(nums)):
            pre[i] =pre[i-1] * nums[i-1]
        suf = {}
        suffix = 1
        suf[len(nums)-1] = 1
        for i in range(len(nums)-2,-1,-1):
            suf[i] = suf[i+1] * nums[i+1]
        for i in range(len(nums)):
            res[i]=(pre[i]*suf[i])
        return res