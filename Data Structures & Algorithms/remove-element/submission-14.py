class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        if len(nums) == 1:
            if nums[0] == val:
                return 0
            return 1
        start = 0
        end = len(nums) - 1

        while (start <= end):
            while (end > -1 and nums[end] == val):
                end -= 1
            if start <= end:
                if nums[start] == val:
                    nums[start], nums[end] = nums[end], nums[start]
                start += 1
        return start
