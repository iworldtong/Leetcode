#!/usr/bin/env python

class Solution:
    def removeKdigits(self, num, k):
        """
        :type num: str
        :type k: int
        :rtype: str
        """
        nl = [int(n) for n in num]

        p = 0

        for i in range(k):
            if k - i == len(nl):
                return "0"

            for j in range(p, len(nl)):
                if j == len(nl) - 1:
                    nl.pop(j)
                    p = j - 1
                    break
                elif nl[j] > nl[j + 1]:
                    nl.pop(j)
                    p = max(0, j - 1)
                    break


        res = ""
        for i in range(len(nl)):
            if len(res) == 0 and nl[i] == 0:
                continue
            res += str(nl[i])


        return res if len(res) > 0 else "0"





if __name__ == '__main__':
    tests = [
        {'num':"1432219", 'k': 3}, # "1219"
        {'num':"10200", 'k': 1},   # "200"
        {'num':"10", 'k': 2},      # "0"

    ]

    s = Solution()

    for t in tests:
        print(s.removeKdigits(t['num'], t['k']))