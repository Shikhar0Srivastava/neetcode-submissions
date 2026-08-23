class Solution:
    def findMin(self, nums: List[int]) -> int:
        if len(nums) < 2:
            return nums[0]
        if len(nums) == 2:
            return nums[0] if nums[0] < nums[1] else nums[1]

        total_min = float("inf")
        start = 0
        end = len(nums) - 1

        while(start < end):
            if nums[start] < nums[end]:
                total_min = min(total_min, nums[start])
                break
            mid = start + ((end - start) // 2)
            total_min = min(total_min, nums[mid])
            if nums[start] < nums[mid]:
                start = mid + 1
            else:
                end = mid - 1
        return total_min
        