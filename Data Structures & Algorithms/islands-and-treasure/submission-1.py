class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        INF = 2147483647

        n, m = len(grid), len(grid[0])

        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]

        q = deque()

        for i in range(n):
            for j in range(m):
                if grid[i][j] == 0:
                    q.append((i, j))
            
        while q:
            r, c = q.popleft()
            for dr, dc in directions:
                dr += r
                dc += c

                if dr in range(n) and dc in range(m) and grid[dr][dc] != -1 and grid[dr][dc] > grid[r][c] + 1:
                    grid[dr][dc] = 1 + grid[r][c]
                    q.append((dr, dc))
        

        