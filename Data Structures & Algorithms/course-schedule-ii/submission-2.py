class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = defaultdict(list)
        count = defaultdict(int)

        for course, pre in prerequisites:
            graph[pre].append(course)
            count[course] += 1
        
        stack = []
        #visited = set()

        for course in range(numCourses):
            if count[course] == 0:
                stack.append(course)
                #visited.add(course)
        
        res = []

        while stack:
            curr = stack.pop()
            res.append(curr)

            for course in graph[curr]:
                count[course] -= 1
                if count[course] == 0:
                    #visited.add(course)
                    stack.append(course)
        
        return res if len(res) == numCourses else []



        

        