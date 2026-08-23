class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        if len(s) < 2:
            return len(s)
        if len(s) == 2:
            return 2 if k > 0 or s[0] == s[1] else 1
        l = 0
        r = 0
        max_length = 1
        replacements = 0
        while (r < len(s)):
            if s[l] != s[r]:
                replacements += 1
            while (replacements > k):
                while s[l] != s[r]:
                    replacements -= 1
                    l += 1
                l += 1
            max_length = max(max_length, r - l + 1)
            r += 1
        return max_length
        