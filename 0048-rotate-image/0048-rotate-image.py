class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        result = [] #ez
        k = 0
        n = len(matrix)
        while k<n: 
            for i in range(n-1,-1,-1): 

                result.append(matrix[i][k])
            
            matrix.append(result) 




            k+=1
            result =[]
        del matrix[:n]