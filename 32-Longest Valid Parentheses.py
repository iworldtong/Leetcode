#!/usr/bin/env python

class Solution:
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        if len(s) == 0: return 0
        dp = [0 for i in range(len(s)) if True]

        for i in range(1, len(s)):
            if s[i] == ')':
                dp1 = 0
                dp2 = 0
                if s[i-1] == '(':
                    dp1 = 2 + dp[i-2]
                elif i-dp[i-1]-1 >= 0 and s[i-dp[i-1]-1] == '(':
                    dp2 = 2 + dp[i-1] + dp[i-dp[i-1]-2]
                dp[i] = max(dp1, dp2)
            print(dp)
        return max(dp)







if __name__ == '__main__':
    test = "(()())" # 6


    s = Solution()
    print(s.longestValidParentheses(test))