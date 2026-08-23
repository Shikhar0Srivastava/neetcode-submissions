class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if not n:
            return True
        adj = {i:[] for i in range(n)}

        for first, second in edges:
            adj[first].append(second)
            adj[second].append(first)

        visited = set()

        def dfs(node, prev):
            if node in visited:
                return False
            visited.add(node)

            for nei in adj[node]:
                if nei != prev:
                    if not dfs(nei, node):
                        return False
            return True
        
        
        return dfs(0, -1) and len(visited) == n

        