class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = [(x**2 + y**2, x, y) for x, y in points]
        heapq.heapify(heap)

        print(heap)

        ret = []

        for _ in range(k):
            curr = heapq.heappop(heap)
            ret.append([curr[-2], curr[-1]])
        
        return ret
        