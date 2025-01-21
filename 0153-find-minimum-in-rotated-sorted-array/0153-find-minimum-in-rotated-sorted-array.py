class Solution:
    def findMin(self, nums: List[int]) -> int:
        if(len(nums)<=3):
            return min(nums)
        l=0
        r=len(nums)-1
        while(l<=r and len(nums)>=3):
            mid = (r-l)//2+l
            print(l,r,mid)
            if(nums[l]<nums[mid]):
                l=mid
            elif(nums[l]>nums[mid]):
                r=mid
            else:
                if(l+1==r and nums[l]>nums[r]):
                    return nums[r]
                else:
                    return min(nums[0],nums[len(nums)-1]) 
        return -1