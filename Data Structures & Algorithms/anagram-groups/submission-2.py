class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = {}
        for string in strs:
            char_array = [0] * 26
            for c in string:
                char_array[ord(c) - ord('a')] += 1
            
            if str(char_array) in anagrams:
                anagrams[str(char_array)].append(string)
            else:
                anagrams[str(char_array)] = [string]
        ans = []
        for key in anagrams:
            ans.append(anagrams[key])
        return ans