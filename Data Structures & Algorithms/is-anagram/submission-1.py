class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        hash_table = [0] * 26
        for c in s:
            hash_table[ord(c) - ord('a')] += 1
        for c in t:
            hash_table[ord(c) - ord('a')] -= 1
        for i in hash_table:
            if i != 0:
                return False
        return True