class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not s or not t or len(s) < len(t):
            return ""
        t_map = {}
        s_map = {}
        for ch in t:
            t_map[ch] = t_map.get(ch, 0) + 1
        have = 0
        need = len(t_map)
        min_length = float("inf")
        min_string = ""
        l = 0
        r = 0

        while(r < len(s)):
            s_map[s[r]] = s_map.get(s[r], 0) + 1

            if s[r] in t_map and t_map[s[r]] == s_map[s[r]]:
                have += 1
            while have == need:
                if r - l + 1 < min_length:
                    min_length = r - l + 1
                    min_string = s[l: r + 1]
                s_map[s[l]] -= 1
                if s[l] in t_map and s_map[s[l]] < t_map[s[l]]:
                    have -=1
                l += 1
            r += 1
        return min_string