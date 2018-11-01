#!/usr/bin/env python

class Solution:
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        if m == 0 or n == 0: return 0

        dp = [1 for i in range(n) if True]

        for i in range(1,m):
            for j in range(n):
                if j == 0:
                    dp[j] = 1
                else:
                    dp[j] += dp[j-1] 



        return dp[-1]






if __name__ == '__main__':
    m = 3; n = 2

    s = Solution()
    print(s.uniquePaths(m,n))