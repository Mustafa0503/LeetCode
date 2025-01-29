class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        dq = collections.deque()
        if(k==1):
            return nums
        c=0

        l,r=0,0
        ans = []
        while(r<len(nums)):

            while(dq and nums[r]>dq[-1]):
                dq.pop()
            dq.append(nums[r])
            if(r>=k-1):
                ans.append(dq[0])
            if(nums[l]==dq[0]and r>=k-1):

                dq.popleft()

            if(r>=k-1):
                l+=1
            r+=1
        return ans