class Solution:
    def countDays(self, days: int, meetings: List[List[int]]) -> int:
        meetings = sorted(meetings, key = lambda x: x[0])
        res = []

        for i in range(len(meetings)):
            curr = meetings[i]
            if res and res[-1][1]>= curr[0]:
                res[-1][1] = max(res[-1][1], curr[1])
            else:
                res.append(curr)
        ret = 0
        #print(res)
        for x,y in res:
            ret += y-x+1


        return days - ret

