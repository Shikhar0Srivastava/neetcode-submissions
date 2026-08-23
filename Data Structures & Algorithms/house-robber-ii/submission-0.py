class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]
        if len(nums) == 2:
            return nums[0] if nums[0] > nums[1] else nums[1]
        
        return max(self.helper(nums[1:]), self.helper(nums[:-1]))

    def helper(self, nums):
        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]
        if len(nums) == 2:
            return nums[0] if nums[0] > nums[1] else nums[1]
        
        rob1 = rob2 = 0

        for n in nums:
            temp = max(n + rob1, rob2)
            rob1 = rob2
            rob2 = temp
        return rob2
        