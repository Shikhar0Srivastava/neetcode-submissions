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
        max_freq = 0
        freq_map = {}
        while (r < len(s)):
            freq_map[s[r]] = freq_map.get(s[r], 0) + 1
            max_freq = max(max_freq, freq_map[s[r]])
            while((r - l + 1) - max_freq > k):
                freq_map[s[l]] -= 1
                l += 1
            max_length = max(max_length, r - l + 1)
            r += 1
        return max_length
        