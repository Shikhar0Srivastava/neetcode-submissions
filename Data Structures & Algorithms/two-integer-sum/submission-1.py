class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_map = {}
        for i in range(len(nums)):
            val = nums[i]
            if target - val in num_map:
                return [num_map.get(target - val), i]
            num_map[val] = i
        return [-1, -1]