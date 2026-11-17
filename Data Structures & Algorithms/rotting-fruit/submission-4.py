class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        n, m = len(grid), len(grid[0])
        times = [[float("inf")] * m for _ in range(n)]

        q = deque()

        for i in range(n):
            for j in range(m):
                if grid[i][j] == 2:
                    q.append((i, j))
                    times[i][j] = 0

        #print(times)
        #print(q)

        directions = [[-1, 0], [1, 0], [0, 1], [0, -1]]
        while q:
            r, c = q.popleft()
            time = times[r][c] + 1
            for x, y in directions:
                x += r
                y += c
                if (x in range(n)) and y in range(m) and grid[x][y] == 1 and times[x][y] > time:
                    #print(x, y)
                    times[x][y] = time
                    q.append((x, y))
        
        print(times)
    
        res = 0
        for i in range(n):
            for j in range(m):
                if grid[i][j] != 0:
                    res = max(res, times[i][j])

        return -1 if res == float("inf") else res
        

        