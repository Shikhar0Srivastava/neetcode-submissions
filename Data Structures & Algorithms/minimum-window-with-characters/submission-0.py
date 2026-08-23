class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not s or not t or len(s) < len(t):
            return ""
        t_map = {}
        s_map = {}
        for ch in t:
            t_map[ch] = t_map.get(ch, 0) + 1
        l = 0
        r = 0
        min_length = float("inf")
        min_string = ""
        count_chars = 0
        while (r < len(s)):
            if s[r] in t_map:
                s_map[s[r]] = s_map.get(s[r], 0) + 1
                if s_map[s[r]] == t_map[s[r]]:
                    count_chars += 1
            if count_chars == len(t):
                if r - l + 1 < min_length:
                    min_length = r - l + 1
                    min_string = s[l:r + 1]
            while(count_chars == len(t)):
                if s[l] in t_map:
                    s_map[s[l]] -= 1
                    if s_map[s[l]] < t_map[s[l]]:
                        count_chars -= 1
                l += 1
            r += 1
        if r - l + 1 < min_length:
            min_length = r - l + 1
            min_string = s[l-1:r+1]
        return min_string