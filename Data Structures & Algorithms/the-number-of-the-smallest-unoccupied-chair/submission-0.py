class Solution:
    def smallestChair(self, times: List[List[int]], targetFriend: int) -> int:
        occupied = []
        chairs = []

        arrival = times[targetFriend][0]

        times = sorted(times, key = lambda x: x[0])

        #print(times, arrival)

        for start, end in times:
            while occupied and occupied[0][0] <= start:
                _, chair = heapq.heappop(occupied)
                heapq.heappush(chairs, chair)
            
            chair = len(occupied)
            if chairs:
                chair = min(chair, heapq.heappop(chairs))
            
            heapq.heappush(occupied, (end, chair))
            #print("occupied", occupied)
            #print("chairs", chairs)

            if start == arrival:
                return chair



