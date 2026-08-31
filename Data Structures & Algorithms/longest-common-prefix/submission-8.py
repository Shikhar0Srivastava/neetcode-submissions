class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = strs[0]
        for string in strs[1:]:
            index = 0
            while index < min(len(prefix), len(string)):
                if prefix[index] != string[index]:
                    break
                index += 1
            prefix = prefix[:index]
        return prefix