class Solution:
    def threeSum(self, arr: List[int]) -> List[List[int]]:
        dic = {}
        arr.sort()
        res = []

        for i in range(len(arr)):
            if((i>0 and arr[i-1]!=arr[i]) or i==0):
                l = i+1
                r = len(arr)-1

                while(l<r):

                    if(arr[l]+arr[i] + arr[r]==0):
                        res.append([arr[i],arr[l],arr[r]])
                        l=l+1
                        
                        while(arr[l]==arr[l-1] and l<r):
                            l=l+1
                    elif(arr[l]+arr[r]+arr[i]>0):
                        r = r -1
                    elif(arr[l]+arr[r]+arr[i]<0):
                        l = l+1


                    

        return res