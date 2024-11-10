
def printMatrix(self, matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            print(matrix[i][j], end=" ")
        print()
def convert(self, s, numRows):
    """
    :type s: str
    :type numRows: int
    :rtype: str
    """
    j=0
    fin=""
    pointer = 0
    o=0
    i=0
    if(numRows==1):
        return s
    matrix = [[0 for j in range(len(s)//numRows+numRows)] for i in range(numRows)]
    while i<len(s):
        print(i,j)
        if(o==0):
            while j < numRows:
                if(pointer<len(s)):
                    
                    matrix[j][i] = s[pointer]
                    pointer += 1

                j+=1
            j=0
            o+=1
            i+=1
            
        else:
            
            o=numRows-2
            while o > 0:
                if(pointer<len(s)):
                    matrix[o][i] = s[pointer]
                    pointer += 1
                o-=1
                i+=1
    for m in range(len(matrix)):
        for n in range(len(matrix[m])):

            if(matrix[m][n] != 0):
                fin += matrix[m][n]
    printMatrix(0,matrix)
    return fin
# ar = [["s","a"],["c","h"]]

# for i in range(len(ar)):
#     for j in range(len(ar[i])):
#         ar[i][j] = 0
#     print()
# for i in range(len(ar)):
#     for j in range(len(ar)):
#         print(ar[j][i], end=" ")
#     print() 
s= "PAYPALISHIRING"
print(convert(0,s,7))
