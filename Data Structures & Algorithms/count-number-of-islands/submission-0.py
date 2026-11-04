class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        visited = set()

        n, m = len(grid), len(grid[0])

        def bfs(i, j):
            nonlocal visited
            visited.add((i, j))
            for x, y in [[0, 1], [0, -1], [1, 0], [-1, 0]]:
                x += i
                y += j
                if x < 0 or x > n-1 or y < 0 or y > m-1:
                    continue
                if grid[x][y] == "1" and (x,y) not in visited:
                    bfs(x, y)
            
        ret = 0
        for i in range(n):
            for j in range(m):
                if grid[i][j] == "1" and (i, j) not in visited:
                    bfs(i, j)
                    ret += 1
        
        return ret
        