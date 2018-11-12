#!/usr/bin/env python

# Definition for an interval.
# class Interval:
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution:
    def eraseOverlapIntervals(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: int
        """
        N = len(intervals)
        if N < 2: return 0

        intervals.sort(key=lambda x: [x.end, x.start])
        cnt = 0
        m = intervals[0].end
        for i in range(1,N):
            if m > intervals[i].start:
                cnt += 1
            else:
                m = intervals[i].end

        return cnt


