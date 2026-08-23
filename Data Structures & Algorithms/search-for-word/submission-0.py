class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        num_rows = len(board)
        num_cols = len(board[0])
        path = set()

        def dfs(curr_row, curr_col, i):
            if i == len(word):
                return True
            if curr_row < 0 or curr_row >= num_rows:
                return False
            if curr_col < 0 or curr_col >= num_cols:
                return False
            if word[i] != board[curr_row][curr_col]:
                return False
            if (curr_row, curr_col) in path:
                return False

            path.add((curr_row, curr_col))
            ans = (dfs(curr_row - 1, curr_col, i + 1) or
                    dfs(curr_row + 1, curr_col, i + 1) or
                    dfs(curr_row, curr_col - 1, i + 1) or
                    dfs(curr_row, curr_col + 1, i + 1))
            path.remove((curr_row, curr_col))
            return ans
        
        for curr_row in range(num_rows):
            for curr_col in range(num_cols):
                if dfs(curr_row, curr_col, 0):
                    return True
        return False