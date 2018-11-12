#!/usr/bin/env python

class Solution:
    def findMinArrowShots(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        N = len(points)
        if N < 2: return N

        points.sort(key=lambda x: [x[0], x[1]])

        cnt = 1
        min_p = points[0][1]
        for i in range(1,N):
            if points[i][0] > min_p:
                cnt += 1
                min_p = points[i][1]
            else:
                min_p = min(min_p, points[i][1])


        return cnt





if __name__ == '__main__':
    points = [[9,12],[1,10],[4,11],[8,12],[3,9],[6,9],[6,7]] # 2

    s = Solution()
    print(s.findMinArrowShots(points))