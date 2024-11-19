class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d={}
        for i in range(len(strs)):
            k = "".join(sorted(strs[i]))
            if(k in d):
                d[k].append(strs[i])
            else:
                d[k] = [strs[i]]
        print(d.values())
        return list(d.values())