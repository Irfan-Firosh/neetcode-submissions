class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals = sorted(intervals,key=lambda x: x[0])

        n = len(intervals)
        res = []
        res.append(intervals[0])

        for i in range(1, n):
            if intervals[i][0] <= res[-1][1]:
                #print(i)
                prev_start, prev_end = res.pop()
                res.append([prev_start, max(intervals[i][1], prev_end)])
            else:
                res.append(intervals[i])


        return res
                        