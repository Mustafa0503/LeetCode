class Solution:
    def findMin(self, nums: List[int]) -> int:
        if(len(nums)<=2):
            return min(nums)
        l=0
        r=len(nums)-1
        while(1):
            mid = (r-l)//2+l
            if(nums[l]<nums[mid]):
                l=mid
            elif(nums[l]>nums[mid]):
                r=mid
            else:
                if(nums[l]>nums[r]):
                    return nums[r]
                else:
                    return min(nums[0],nums[len(nums)-1]) 
        return -1