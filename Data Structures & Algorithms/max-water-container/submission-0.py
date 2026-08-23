class Solution:
    def maxArea(self, heights: List[int]) -> int:
        start = 0
        end = len(heights) - 1
        max_water = 0
        while(start < end):
            water = (end - start) * min(heights[start], heights[end])
            max_water = max(water, max_water)
            if (heights[start] < heights[end]):
                start += 1
            else:
                end -= 1
        return max_water
        