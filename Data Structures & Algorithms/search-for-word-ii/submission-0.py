class TrieNode:
    def __init__(self):
        self.root = {}
    
    def add_word(self, word):
        curr = self.root
        for ch in word:
            if ch not in curr:
                curr[ch] = {}
            curr = curr[ch]
        curr['*'] = {}

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        trie = TrieNode()
        for word in words:
            trie.add_word(word)
        
        num_rows = len(board)
        num_cols = len(board[0])

        result = set()
        visited = set()

        def dfs(curr_row, curr_col, node, curr_word):
            if curr_row < 0 or curr_row >= num_rows:
                return
            if curr_col < 0 or curr_col >= num_cols:
                return
            if (curr_row, curr_col) in visited:
                return
            if board[curr_row][curr_col] not in node:
                return
            
            visited.add((curr_row, curr_col))
            node = node[board[curr_row][curr_col]]
            curr_word += board[curr_row][curr_col]

            if '*' in node:
                result.add(curr_word)

            dfs(curr_row - 1, curr_col, node, curr_word)
            dfs(curr_row + 1, curr_col, node, curr_word)
            dfs(curr_row, curr_col - 1, node, curr_word)
            dfs(curr_row, curr_col + 1, node, curr_word)

            visited.remove((curr_row, curr_col))

        for curr_row in range(num_rows):
            for curr_col in range(num_cols):
                dfs(curr_row, curr_col, trie.root, "")
        
        return list(result)
            



        