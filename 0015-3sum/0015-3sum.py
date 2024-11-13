class Solution:
    def threeSum(self, arr: List[int]) -> List[List[int]]:
        arr.sort()
        res = []

        for i,a in enumerate(arr):
            if((i>0 and arr[i-1]==a)):
                continue
            l = i+1
            r = len(arr)-1

            while(l<r):
                summm = arr[l]+arr[i] + arr[r]
                if(summm==0):
                    res.append([arr[i],arr[l],arr[r]])
                    l=l+1
                    
                    while(arr[l]==arr[l-1] and l<r):
                        l=l+1
                elif(summm>0):
                    r = r -1
                elif(summm<0):
                    l = l+1


                    

        return res  