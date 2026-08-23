class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        ans = 1
        max_product = 1
        min_product = 1

        for num in nums:
            temp = max_product * num

            max_product = max(temp, min_product * num, num)
            min_product = min(temp, min_product * num, num)
            ans = max(ans, max_product)
        return ans
        