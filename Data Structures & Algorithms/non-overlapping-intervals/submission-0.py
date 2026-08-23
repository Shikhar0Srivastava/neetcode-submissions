class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        res = 0
        prevEnd = intervals[0][1]
        for i in range(1, len(intervals)):
            interval = intervals[i]
            if interval[0] >= prevEnd:
                prevEnd = interval[1]
            else:
                res += 1
                prevEnd = min(interval[1], prevEnd)
        return res
        