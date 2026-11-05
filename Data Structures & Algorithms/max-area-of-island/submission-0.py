class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        visited = set()
        n, m = len(grid), len(grid[0])

        ret = 0

        def bfs(i, j):
            directions = [[-1, 0], [1,0], [0,1], [0,-1]]

            q = deque([(i,j)])
            area = 1

            while q:
                r, c = q.popleft()

                for dr, dc in directions:
                    dr += r
                    dc += c
                    if dr in range(n) and dc in range(m) and grid[dr][dc] == 1 and (dr, dc) not in visited:
                        visited.add((dr, dc))
                        area += 1
                        q.append((dr, dc))
            
            return area

        
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1 and (i, j) not in visited:
                    visited.add((i, j))
                    ret = max(bfs(i, j), ret)
        
        return ret

            

        