class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        ans = [0 for x in range(2 * len(nums))]
        for i in range(len(nums)):
            ans[i] = nums[i]
            ans[i + len(nums)] = nums[i]

        return ans