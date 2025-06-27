class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        result = []
        for x,y in points:
            dist = math.sqrt(x**2 + y**2)#because x1 and y1 are always 0 in our case.so sqr(0-(x))=sqr(x)
            heapq.heappush(heap, (dist,x,y))
        for _ in range(k):
            d,x,y = heapq.heappop(heap)
            result.append([x,y])
        return result