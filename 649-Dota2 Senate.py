#!/usr/bin/env python

class Solution:
    def predictPartyVictory(self, senate):
        """
        :type senate: str
        :rtype: str
        """
        d = {'R': "Radiant", 'D': "Dire"}

        s = list(senate)
        i = 0
        j = 1
        c = 1
        N = len(s)
        while i != j and N > 1:
            if s[i] != s[j]:
                s.pop(j)
                N -= 1
                c -= 1
                if c < 1:
                    i = j
                    j += 1
                    c = 1
                else:
                    if i > j:
                        i -= 1
            else:
                c += 1
                j += 1
            i %= N
            j %= N


        return d[s[0]]




if __name__ == '__main__':
    senate = "RD"
    
    s = Solution()
    print(s.predictPartyVictory(senate))
