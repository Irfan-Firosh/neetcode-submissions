class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = [-1*s for s in stones]
        heapq.heapify(heap)

        while len(heap) > 1:
            a = -1*heapq.heappop(heap)
            b = -1*heapq.heappop(heap)

            if a == b:
                continue
            heapq.heappush(heap, -max(a,b)+min(a,b))
            
            #print(heap)
        
            
        return -1*heap[0] if heap else 0
        