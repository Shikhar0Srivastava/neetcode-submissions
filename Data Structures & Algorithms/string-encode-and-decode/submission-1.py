class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = ""
        for string in strs:
            encoded += f"{len(string)}#{string}"
        return encoded

    def decode(self, s: str) -> List[str]:
        ans = []
        length = 0
        curr = 0
        while (curr < len(s)):
            if s[curr] != '#':
                length *= 10
                length += int(s[curr])
                curr += 1
            else:
                ans.append(s[curr + 1: curr + length + 1])
                curr = curr + 1 + length
                length = 0
        return ans

