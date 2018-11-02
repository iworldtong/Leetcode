#!/usr/bin/env python

class Solution:
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        M = len(grid)
        N = len(grid[0])

        dp = [grid[0][0]]
        for m in range(1,M):
            dp.append(dp[m-1] + grid[m][0])


        for n in range(1,N):
            dp[0] += grid[0][n]
            for m in range(1,M):
                dp[m] = min(dp[m-1], dp[m]) + grid[m][n]


        return dp[-1]





if __name__ == '__main__':
    test =[[1,2],[1,1]]



    s = Solution()
    print(s.minPathSum(test))