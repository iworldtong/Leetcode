#!/usr/bin/env python


class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        M = len(obstacleGrid)
        N = len(obstacleGrid[0])

        dp = [0 for i in range(M) if True]
        dp[0]=1


        for j in range(N):
            for i in range(M):
                if obstacleGrid[i][j] == 0:
                    if i != 0:
                        dp[i] += dp[i-1] 
                else:
                    dp[i]=0

        return dp[-1]






if __name__ == '__main__':
    test = [[0,1,0,0,0],[1,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0]]


    s = Solution()
    print(s.uniquePathsWithObstacles(test))