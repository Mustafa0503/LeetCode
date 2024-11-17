class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        fin = ""
        j=1
        k=1
        q=9
        temp=""
        if s == None or len(s) == 0:
            return ""
        if len(s) == 1:
            return s
        for i in range(len(s)):
            
            while i-j>=0 and i+k<len(s):
                
                if s[i-j] == s[i+k]:

                    j+=1
                    k+=1
                else:
                    break
            temp = s[i-j+1:i+k]
            if(len(temp)>len(fin)):
                fin = temp
            j=0
            k=1
            while i-j>=0 and i+k<len(s):
                
                if s[i-j] == s[i+k]:

                    j+=1
                    k+=1
                else:
                    break
            temp = s[i-j+1:i+k]
            if(len(temp)>len(fin)):
                fin = temp
            j=1
            k=1
        return fin
   