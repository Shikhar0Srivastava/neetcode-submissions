class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) < 2:
            return len(s)
        if len(s) == 2:
            return 1 if s[0] != s[1] else 2
        
        l = 0
        r = 0
        max_length = 1

        curr_set = set()

        while(r < len(s)):
            while(s[r] in curr_set):
                curr_set.remove(s[l])
                l += 1
            curr_set.add(s[r])
            max_length = max(max_length, r - l + 1)
            r += 1
            
            

        return max_length
                
