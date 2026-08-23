class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        last_row = [1] * n

        for i in range(m - 1):
            newRow = [1] * n
            for j in range(n - 2, -1, -1):
                newRow[j] = newRow[j + 1] + last_row[j]
            last_row = newRow
        
        return last_row[0]
