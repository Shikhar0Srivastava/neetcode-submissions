class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = {i:False for i in range(len(s))}
        
        def dfs(i):
            if i == len(s):
                return True
            for word in wordDict:
                length = len(word)
                if (i + length) <= len(s) and s[i:i + length] == word:
                    dp[i] = True
                    if dfs(i + length):
                        return True
            return False

        return dfs(0)
                


        