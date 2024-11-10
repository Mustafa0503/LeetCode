class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        x=0
        y=len(nums)-1
        for i in range(len(nums)):
            while(x<len(nums)and y>=0):
                print(i,x,y)
               
                if(i!=x!=y and nums[x]+nums[y]+nums[i] == 0):
                    res.append(nums[x]+nums[y]+nums[i])
                    

                x+=1
                y-=1
            x=0
            y=len(nums)-1
        return res
    print(threeSum(0,[-1,0,1,2,-1,-4]))