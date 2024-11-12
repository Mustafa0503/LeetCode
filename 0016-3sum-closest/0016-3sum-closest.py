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

                # print(i,l,r)
                if(summm==target):
                    return target
                    l=l+1
                    
                    while(arr[l]==arr[l-1] and l<r):
                        l=l+1
                elif(summm>target):
                    t = abs((arr[l]+arr[r]+arr[i]-target))
                    if(abs(ress)>t):
                        ress = t
                        fin = summm
                    r = r -1
                elif(summm<target):
                    
                    t = abs((arr[l]+arr[r]+arr[i]-target))

                    if(abs(ress)>t):
    
                        ress = t
                        fin = summm
                    l = l+1
                # ?print(summm, ress,fin)
        return fin