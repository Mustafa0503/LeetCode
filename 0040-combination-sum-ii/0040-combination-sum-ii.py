class Solution:
    #opt sol same shit loopin a bit diff
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()  # sort to handle duplicates easily

        def dfs(start, curr, total):
            # Base cases
            if total == target:
                res.append(curr[:])
                return
            if total > target:
                return

            prev = -1  # track previous candidate to skip duplicates
            for i in range(start, len(candidates)):
                if candidates[i] == prev:
                    continue  # skip duplicate numbers on same depth level
                curr.append(candidates[i])
                dfs(i + 1, curr, total + candidates[i])  # move to next index
                curr.pop()
                prev = candidates[i]

        dfs(0, [], 0)
        return res
