class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        sub=""
        d = defaultdict(int)
        longest=1
        for i in range(len(s)):
            d[s[i]]+=1
            sub = sub+s[i]
            if(len(sub)-max(d.values())>k):
                d[sub[0]]-=1
                sub = sub[1:]
            longest = max(longest,len(sub))
        return longest