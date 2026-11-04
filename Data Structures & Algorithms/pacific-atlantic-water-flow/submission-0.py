class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        # have one for pacific and one for atlantic

        n, m = len(heights), len(heights[0])

        def traverse(arr, visited):
            q = deque(arr)
            visited.update((r, c) for r,c in arr)

            while q:
                r, c = q.popleft()
                directions = [[0,1], [0,-1], [1,0], [-1, 0]]

                for dr, dc in directions:
                    dr += r
                    dc += c
                    if (dr in range(n) and dc in range(m) and (dr, dc) not in visited
                    and heights[dr][dc] >= heights[r][c]):
                        q.append([dr, dc])
                        visited.add((dr, dc))
            
            return visited
                    
            

        #pacific first
        pacific = []
        for j in range(m):
            pacific.append((0, j))
        
        for i in range(1, n):
            pacific.append((i, 0))
        
        pacific = traverse(pacific, set())

        atlantic = []
        for j in range(m):
            atlantic.append((n-1, j))
        
        for i in range(n-1):
            atlantic.append((i, m-1))
        
        atlantic = traverse(atlantic, set())

        ret = pacific & atlantic
        return [[x,y] for x,y in ret]
        
        