class Solution:
    def threeSum(self, arr: List[int]) -> List[List[int]]:
        dic = {}

        for index, val in enumerate(arr):
            dic[val] = index
        res = []
        for i in range(len(arr)):

            for j in range(i, len(arr)):
                
                temp = dic.get((-1*(arr[i]+arr[j])))
                
                if(temp != None and i != j and i != temp and j != temp):
                    
                    lis=sorted([arr[i],arr[temp],arr[j]])
                    if( lis not in res):
                        res.append(lis)
                    

        return res