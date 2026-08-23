class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        
        num_rows = len(grid)
        num_cols = len(grid[0])

        visited = set()
        islands = 0

        def bfs(row, col):
            q = collections.deque()
            visited.add((row, col))
            q.append((row, col))

            while q:
                curr_row, curr_col = q.popleft()
                directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
                for r, c in directions:
                    new_r = curr_row + r
                    new_c = curr_col + c

                    if (new_r in range(num_rows) and
                        new_c in range(num_cols) and
                        grid[new_r][new_c] == "1" and
                        (new_r, new_c) not in visited):
                        q.append((new_r, new_c))
                        visited.add((new_r, new_c))


        for row in range(num_rows):
            for col in range(num_cols):
                if grid[row][col] == '1' and (row, col) not in visited:
                    bfs(row, col)
                    islands += 1
        return islands
                    

        