class Solution:
    def threeSum(self, arr: List[int]) -> List[List[int]]:
        ans=[]
        arr.sort()
        for i in range(len(arr)):
            if(i!=0 and arr[i]==arr[i-1]):
                continue
            j=i+1
            k=len(arr)-1
            while j<k:
                total_sum=arr[i]+arr[j]+arr[k]
                if(total_sum<0):#increase the elements(total_sum) value
                    j+=1
                elif(total_sum>0):#decrease the elements(total_sum) value
                    k-=1
                else:
                    temp=[arr[i],arr[j],arr[k]]
                    ans.append(temp)
                    j+=1
                    k-=1
                    while(j<k and arr[j]==arr[j-1]):
                        j+=1
                    while(j<k and arr[k]==arr[k+1]):
                        k-=1
        return ans     