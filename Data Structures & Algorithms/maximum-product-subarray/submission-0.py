class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        ans = 1
        max_product = 1
        min_product = 1

        for num in nums:
            max_product *= num
            min_product *= num

            max_product = max(max_product, min_product, num)
            min_product = min(max_product, min_product, num)
            ans = max(ans, max_product)
        return ans
        