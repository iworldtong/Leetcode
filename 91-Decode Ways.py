#!/usr/bin/env python

class Solution:
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        ns = len(s)
        if ns == 0: return 0

        dp = [0 for i in range(ns)]

        for i in range(ns):
            if i == 0:
                if s[i] != "0":
                    dp[i] = 1
            else:
                if s[i] != "0":
                    dp[i] = dp[i-1]
                if int(s[i-1:i+1]) in range(10,27):
                    if i > 1:
                        dp[i] += dp[i-2]
                    else:
                        dp[i] += 1

        return dp[-1]




if __name__ == '__main__':
    test = "226" # 3



    s = Solution()
    print(s.numDecodings(test))