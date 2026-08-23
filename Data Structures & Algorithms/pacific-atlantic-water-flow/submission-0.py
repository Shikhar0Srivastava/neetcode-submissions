class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        pacific = set()
        atlantic = set()

        num_rows = len(heights)
        num_cols = len(heights[0])

        def dfs(r, c, visited, prev_height):
            if (r, c) in visited:
                return
            if (r < 0 or r >= num_rows):
                return
            if (c < 0 or c >= num_cols):
                return
            if (heights[r][c] < prev_height):
                return

            visited.add((r, c))

            dfs(r, c, visit, heights[r][c])
            dfs(r, c, visit, heights[r][c])
            dfs(r, c, visit, heights[r][c])

        for c in range(num_cols):
            dfs(0, c, pacific, heights[0][c])
            dfs(num_rows - 1, c, atlantic, heights[num_rows - 1][c])