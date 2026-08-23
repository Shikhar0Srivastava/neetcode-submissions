class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        curr = 1
        start_products = []
        end_products = []
        for num in nums:
            curr = curr * num
            start_products.append(curr)
        curr = 1
        for i in range(len(nums) - 1, -1, -1):
            curr = curr * nums[i]
            end_products = [curr] + end_products
        ans = [1 for i in range(len(nums))]
        for i in range(len(nums)):
            if i == 0:
                if (i + 1) == len(nums):
                    ans[i] = 1
                else:
                    ans[i] = end_products[i + 1]
            elif i == len(nums) - 1:
                if (i - 1) == -1:
                    ans[i] = 1
                else:
                    ans[i] = start_products[i - 1] 
            else:
                ans[i] = start_products[i - 1] * end_products[i + 1]
        return ans
        