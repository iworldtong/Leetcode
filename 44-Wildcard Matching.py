#!/usr/bin/env python
import pprint
class Solution:
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """

        ns = len(list(s))
        np = len(list(p))

        dp = [False for j in range(ns) if True]

        if ns == 0:
            if p != '*' and np > 0:
                return False
            else:
                return True
        elif np == 0:
            return False 

        idx = 1
        if p[0] == "*":
            for j in range(ns):
                dp[j] = True  
            idx = 0
        elif p[0] == "?" or p[0] == s[0]:
            dp[0] = True  
            
        for i in range(1, np):
            
            if p[i] == '*' and dp[max(idx-1,0)]:
                for k in range(idx-1, ns):
                    dp[max(0, k)] = True 
            else:
                changed = False
                tmp = [False for j in range(ns) if True]
                for j in range(idx, ns):
                    if dp[max(j-1,0)] and (p[i] == '?' or p[i] == s[j]):
                        tmp[j] = True  
                        if changed == False:
                            idx = j + 1 
                            changed = True 
                dp = tmp.copy()


        return dp[-1]




if __name__ == '__main__':

    s = "aa"; p = "aa"  # false

    solution = Solution()
    print(solution.isMatch(s, p))


