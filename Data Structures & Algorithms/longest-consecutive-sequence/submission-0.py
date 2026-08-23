class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        max_len = 0
        len = 0
        for num in nums:
            if (num - 1) in nums:
                continue
            curr = num
            len = 1
            while (curr + 1 in nums):
                len += 1
                curr += 1
            max_len = max(len, max_len)
        return max_len