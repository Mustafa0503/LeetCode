class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        ans=[]
        pre = {}
        prefix = 1
        pre[0]=1
        for i in range(1,len(nums)):
            pre_num = prefix * nums[i-1]
            pre[i] = pre_num
            prefix = pre_num
        suf = {}
        suffix = 1
        suf[len(nums)-1] = 1
        for i in range(len(nums)-2,-1,-1):
            suf_num = suffix * nums[i+1]
            suf[i] = suf_num
            suffix = suf_num
        print(pre)
        print(suf)
        for i in range(len(nums)):
            ans.append(pre[i]*suf[i])
        return ans