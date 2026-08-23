class Solution:
    def isPalindrome(self, s: str) -> bool:
        if len(s) < 2:
            return True
        s = s.lower()
        new_s = ""
        for c in s:
            if c.isalnum():
                new_s += c
        start = 0
        end = len(new_s) - 1
        while(start < end):
            if new_s[start] != new_s[end]:
                return False
            start += 1
            end -= 1
        return True

        