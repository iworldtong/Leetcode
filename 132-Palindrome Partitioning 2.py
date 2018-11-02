#!/usr/bin/env python

class Solution:
    def minCut(self, s):
        """
        :type s: str
        :rtype: int
        """
        sl = list(s)
        sn = len(sl)
        dp = [1 for i in range(sn) if True]

        for i in range(1,sn):
            



        return dp[-1]






if __name__ == '__main__':
    test = "aab"


    s = Solution()
    print(s.minCut(test))