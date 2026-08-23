class Solution:
    def longestPalindrome(self, s: str) -> str:
        res_len = 0
        res = 0
        
        for i in range(len(s)):
            left = right = i
            while left > -1 and right < len(s) and s[left] == s[right]:
                if res_len < right - left + 1:
                    res_len = right - left + 1
                    res = left
                left -= 1
                right += 1

            left = i
            right = i + 1
            while left > -1 and right < len(s) and s[left] == s[right]:
                if res_len < right - left + 1:
                    res_len = right - left + 1
                    res = left
                left -= 1
                right += 1
        
        return s[res:res + res_len]