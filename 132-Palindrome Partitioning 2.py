#!/usr/bin/env python

class Solution:
    def minCut(self, s):
        """
        :type s: str
        :rtype: int
        """
        sl = list(s)
        sn = len(sl)
        dp = [0 for i in range(sn) if True]

        last_l = 1
        for i in range(1,sn):
            dp[i] = dp[i-1] + 1
            for j in range(1,last_l+2):
                if i < j: break
                tmp_s = s[i-j:i+1]
                if tmp_s == tmp_s[::-1]:
                    if i == j:
                        dp[i] = 0
                        last_l = i + 1
                    elif dp[i-j-1] + 1 <= dp[i]:
                        dp[i] = dp[i-j-1] + 1
                        last_l = j + 1

        return dp[-1]






if __name__ == '__main__':
    test = "cabababcbc" # 3


    s = Solution()
    print(s.minCut(test))