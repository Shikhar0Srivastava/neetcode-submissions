class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj = {i:[] for i in range(n)}
        for first, second in edges:
            adj[first].append(second)
            adj[second].append(first)
        
        visited = set()
        ans = 0
        
        def dfs(node):
            if node in visited:
                return
            visited.add(node)

            for nei in adj[node]:
                dfs(nei)
        
        for edge in adj:
            if edge not in visited:
                dfs(edge)
                ans += 1
        return ans

        