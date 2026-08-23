class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        if len(nums) < 3:
            return []
        if len(nums) == 3:
            sum = (nums[0] + nums[1] + nums[2])
            if sum == 0:
                return [nums]
            return []
        ans = set()
        nums.sort()
        for i in range(len(nums) - 2):
            curr = nums[i]
            target = 0 - curr
            start = i + 1
            end = len(nums) - 1
            while(start < end):
                sub_sum = nums[start] + nums[end]
                if sub_sum < target:
                    start += 1
                elif sub_sum > target:
                    end -= 1
                else:
                    ans.add((curr, nums[start], nums[end]))
                    while(start < end and nums[start] == nums[start + 1]):
                        start += 1
                    while(start < end and nums[end] == nums[end - 1]):
                        end -= 1
                    start += 1
                    end -= 1
        return [list(row) for row in ans]