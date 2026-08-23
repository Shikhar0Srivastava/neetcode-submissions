class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj = {i:[] for i in range(numCourses)}
        for course, neighbour in prerequisites:
            adj[course].append(neighbour)

        visited = set()

        def dfs(course, visited):
            if course in visited:
                return False
            if adj[course] == []:
                return True
            visited.add(course)

            for neighbour in adj[course]:
                if not dfs(neighbour, visited):
                    return False
            visited.remove(course)
            adj[course] = []
            return True

        for course in adj:
            return dfs(course, visited)
            
            
        