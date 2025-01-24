class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        sub = ""
        ptr = 0
        longest = 0
        for i in range(len(s)):
            if(s[i] not in sub):
                sub = sub+s[i]
                longest = max(longest, len(sub))
            else:
                ind = sub.find(s[i])
                sub = sub[ind+1:]
                sub  = sub+s[i]
        return longest