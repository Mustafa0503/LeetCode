class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        arr = nums
        arr.sort()
        res = []
        
        ress=abs(nums[0]+nums[1]+nums[2]-target)
        fin=nums[0]+nums[1]+nums[2]
        t = 0
        for i,a in enumerate(arr):
            if((i>0 and arr[i-1]==a)):
                continue
            l = i+1
            r = len(arr)-1
            while(l<r):
                summm = arr[l]+arr[i] + arr[r]
                if(summm==target):
                    return target
                if(abs(ress)>abs(summm - target)):
                    ress = abs(summm -  target)
                    fin = summm
                if(summm>target):
                    r = r -1
                elif(summm<target):
                    l = l+1
                
        return fin