class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if len(nums) < 2:
            return 0 if nums[0] == target else -1
        if len(nums) == 2:
            if nums[0] == target:
                return 0
            if nums[1] == target:
                return 1
            return -1

        start = 0
        end = len(nums) - 1
        res_index = -1

        while(start <= end):
            mid = start + ((end - start) // 2)
            if nums[mid] == target:
                res_index = mid
                break
            if nums[start] <= nums[mid]:
                if nums[start] <= target <= nums[mid]:
                    end = mid - 1
                else:
                    start = mid + 1
            else:
                if nums[mid] <= target <= nums[mid]:
                    start = mid + 1
                else:
                    end = mid - 1
        return res_index
        