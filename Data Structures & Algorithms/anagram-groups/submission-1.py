class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        map = {}
        ans = []
        for string in strs:
            char_array = [0] * 26
            for ch in string:
                char_array[ord(ch) - ord('a')] += 1
            key = tuple(char_array)
            if key in map:
                map[key].append(string)
            else:
                map[key] = [string]
        for key in map:
            ans.append(map.get(key))
        return ans