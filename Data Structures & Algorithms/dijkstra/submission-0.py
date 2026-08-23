class Solution:
    def shortestPath(self, n: int, edges: List[List[int]], src: int) -> Dict[int, int]:
        adj = {}
        for i in range(n):
            adj[i] = []
        for source, dest, weight in edges:
            adj[source].append([dest, weight])

        shortest = {}
        minHeap = [[0, src]]
        while minHeap:
            w1, n1 = heapq.heappop(minHeap)
            if n1 not in shortest:
                shortest[n1] = w1
            
            for n2, w2 in adj[n1]:
                if n2 not in shortest:
                    heapq.heappush(minHeap, [w1 + w2, n2])
        return shortest
