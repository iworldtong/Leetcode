#!/usr/bin/env python

class Solution:
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        ns = len(s)
        nt = len(t)
        if ns == 0: return True

        i = 0
        j = 0

        while j < nt:
            if t[j] == s[i]:
                i += 1
                if i >= ns:
                    return True

            j += 1

        return False



if __name__ == '__main__':
    tests = [
        {"s": "abc", "t": "ahbgdc"}, # True
        {"s": "axc", "t": "ahbgdc"} # False}
    ]

    s = Solution()

    for t in tests:
        print(s.isSubsequence(t['s'],t['t']))

