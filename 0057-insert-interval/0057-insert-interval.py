class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        intervals.append(newInterval)
        result = []
        intervals.sort()
        result.append(intervals[0])
        for i in range(1,len(intervals)):
            if intervals[i][0] >= result[-1][0] and intervals[i][0] <= result[-1][1]:
                if result[-1][1] > intervals[i][1]:
                    continue
                result[-1][1] = intervals[i][1]
            else:
                result.append(intervals[i])
        return result
        