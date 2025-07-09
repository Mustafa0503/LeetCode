class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        intervals.sort(key = lambda i: i[0])

        minHeap = []
        res = {}
        i = 0

        sorted_queries = sorted(queries)

        for q in sorted_queries:
            while  intervals[i][0] <= q:
                l = intervals[i][0]
                r = intervals[i][1]
                heapq.heappush(minHeap, (r-l+1, r))
                i += 1
            
            while minHeap and minHeap[0][1] < q:
                heapq.heappop(minHeap)

            if minHeap:
                res[q] = minHeap[0][0]
            else:
                res[q] = -1

        output = []
        for q in queries:
            output.append(res[q])

        return output
