class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        indices = {}
        for i in range(len(nums)):
            num = nums[i]
            left_value = target - num

            if left_value in indices:
                return [indices[left_value], i]
            
            indices[num] = i
        return [-1, -1]