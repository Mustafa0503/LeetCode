class Solution:
    def minWindow(self, s: str, t: str) -> str:
        def helper(d1, d2):
            for char in d1:
                if d1[char] > d2[char]:
                    return False
            return True
        if len(s) < len(t):
            return ""
        d1 = defaultdict(int)
        for char in t:
            d1[char] += 1
        d2 = defaultdict(int)
        shortest = [0, len(s)]
        l, r = 0, 0
        found = False
        while r < len(s):
            d2[s[r]] += 1
            while helper(d1, d2) and l <= r:
                found = True
                if r - l < shortest[1] - shortest[0]:
                    shortest = [l, r]
                d2[s[l]] -= 1
                l += 1
            r += 1

        if found:
            return s[shortest[0]:shortest[1] + 1]  
        else:
            return ""