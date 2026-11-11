class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:

        in_degree = defaultdict(int)
        graph = defaultdict(list)

        for course, pre in prerequisites:
            in_degree[course] += 1
            graph[pre].append(course)

        visited = set()
        q = deque()

        for c in range(numCourses):
            if in_degree[c] == 0:
                visited.add(c)
                q.append(c)
        
        res = []

        while q:
            pre = q.popleft()
            res.append(pre)

            for c in graph[pre]:
                in_degree[c] -= 1

                if in_degree[c] == 0 and c not in visited:
                    visited.add(c)
                    q.append(c)
        
        return res if len(res) == numCourses else []



        