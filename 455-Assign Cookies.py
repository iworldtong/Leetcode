#!/usr/bin/env python

class Solution:
    def findContentChildren(self, g, s):
        """
        :type g: List[int]
        :type s: List[int]
        :rtype: int
        """
        g_n = len(g)
        s_n = len(s)

        if g_n == 0: return 0

        g.sort()
        s.sort()

        res = 0
        s_i = 0
        for i in range(min(g_n, s_n)):
            for j in range(s_i, s_n):
                if g[i] <= s[j]:
                    res += 1
                    s_i = j + 1
                    break
                if j == s_n - 1:
                    return res

        return res




if __name__ == '__main__':
    g = [1,2,3]; s = [1,1] # 1


    so = Solution()
    print(so.findContentChildren(g, s))