class WordDictionary:

    def __init__(self):
        self.root = {}        

    def addWord(self, word: str) -> None:
        curr = self.root
        for ch in word:
            if ch not in curr:
                curr[ch] = {}
            curr = curr[ch]
        curr['*'] = {}

    def search(self, word: str) -> bool:
        def dfs(index, root):
            curr = root
            for i in range(index, len(word)):
                ch = word[i]
                if ch != '.':
                    if ch not in curr:
                        return False
                    curr = curr[ch]
                else:
                    for child in curr:
                        if child != '*' and dfs(i + 1, curr[child]):
                            return True
                    return False
            return '*' in curr
        return dfs(0, self.root)
                
