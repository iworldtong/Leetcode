#!/usr/bin/env python

class Solution:
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        H = len(triangle)
        if H == 0: return 0

        dp = [[triangle[0][0]]]
        for h in range(1,H):
            floor = triangle[h]
            for i in range(len(triangle[h])):
                if i == 0:
                    floor[i] += dp[-1][0]
                elif i == h:
                    floor[i] += dp[-1][-1]
                else:
                    floor[i] += min(dp[-1][i-1], dp[-1][i])

            dp.append(floor)


        return min(dp[-1])




if __name__ == '__main__':
    test = [
             [2],
            [3,4],
           [6,5,7],
          [4,1,8,3]
        ]



    s = Solution()
    print(s.minimumTotal(test))