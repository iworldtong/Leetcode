#!/usr/bin/env python

class Solution:
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """

        dp = [1 for i in range(n)]

        for i in range(1, n):
            if i == 1:
                dp[i] = 2
            else:
                dp[i] = dp[i-2] + dp[i-1]

        return dp[-1]






if __name__ == '__main__':
    test = 3

    s = Solution()
    print(s.climbStairs(test))