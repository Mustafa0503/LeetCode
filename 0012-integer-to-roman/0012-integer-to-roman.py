class Solution:
    def intToRoman(self, num: int) -> str:
        s = str(num)
        dic = {
            1: "I",
            5: "V",
            10: "X",
            50: "L",
            100: "C",
            500: "D",
            1000: "M"
        }
        k = 1
        res = ""
        for i in range(len(s)-1,-1,-1):
            if(s[i]=="5"):
                key = k*int(s[i])
                res = dic.get(key, "notFound") + res
            elif(s[i]=="9"):
                k*int(s[i])
                ten = 10*k
                one = k

                res =  dic[one] + dic[ten] + res
            elif(s[i]=="4"):
                k*int(s[i])
                ten = 5*k
                one = k

                res =  dic[one] + dic[ten] +res
            elif(int(s[i])>5):
                fiv = 5*k
                
                rep = int(s[i]) - 5
                res = dic[k]*rep + res
                res = dic[fiv] + res
            elif(int(s[i])<5):
                res = dic[k]*int(s[i])+res
                print(2)
            k*=10
        return res
            