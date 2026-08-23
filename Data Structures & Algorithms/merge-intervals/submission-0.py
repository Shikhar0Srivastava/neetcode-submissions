class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        ans = []
        intervals.sort()
        for i in range(len(intervals) - 1):
            if intervals[i][1] < intervals[i + 1][0]:
                ans.append(intervals[i])
            else:
                intervals[i + 1][0] = min(intervals[i][0], intervals[i + 1][0])
                intervals[i + 1][1] = max(intervals[i][1], intervals[i + 1][1])
        ans.append(intervals[-1])
        return ans

        