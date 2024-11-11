class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        arr = sorted(nums)
        ans = []
        

        for i in range(len(arr)-2):
            if i>0 and  arr[i]==arr[i-1]:
                continue

            l =i+1
            r = len(arr)-1

            while l<r:   
                req = arr[i] + arr[l] + arr[r]
                if req<0:
                    l+=1
                elif req>0:
                    r-=1
                else:
                    ans.append([arr[i],arr[l],arr[r]]) 
                    while l<r and arr[l]==arr[l+1]:
                        l+=1
                    while l<r and arr[r]==arr[r-1]:
                        r-=1    
                    l+=1
                    r-=1

        return ans