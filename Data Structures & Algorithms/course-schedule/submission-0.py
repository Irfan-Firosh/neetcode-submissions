class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = defaultdict(list)
        count = defaultdict(int)

        # b->a

        for x, y in prerequisites:
            graph[y].append(x)
            count[x] += 1

        stack = []
        items = 0
        for i in range(numCourses):
            if count[i] == 0:
                stack.append(i)
                items +=1 

        while stack:
            curr = stack.pop()
            for i in graph[curr]:
                count[i] -= 1
                if count[i] == 0:
                    stack.append(i)
                    items += 1
        
        if items != numCourses:
            return False
                
        return True
            

        