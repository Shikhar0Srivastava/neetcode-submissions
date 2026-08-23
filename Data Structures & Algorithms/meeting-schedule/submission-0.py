"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        intervals.sort(key=lambda i: i.start)
        prevEnd = intervals[0].end
        for meeting in intervals[1:]:
            if meeting.start >= prevEnd:
                prevEnd = meeting.end
            else:
                return False
        return True
