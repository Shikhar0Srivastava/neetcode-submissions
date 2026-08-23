class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        
        def dfs(i):
            if i == len(s):
                return True
            for word in wordDict:
                length = len(word)
                if s[i:i + length] == word:
                    if dfs(i + length):
                        return True
            return False

        return dfs(0)
                


        