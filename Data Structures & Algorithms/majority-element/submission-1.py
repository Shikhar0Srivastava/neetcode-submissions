class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        freq = 0
        start = nums[0]
        for i in range(len(nums)):
            if freq == 0:
                start = nums[i]
            if nums[i] == start:
                freq += 1
            else:
                freq -= 1
        return start