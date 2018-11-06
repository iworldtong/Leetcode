#!/usr/bin/env python
import time

class Solution:
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        ns = len(s)
        if len(wordDict) == 0: return []
        wordDict.sort(key=lambda x:len(x))

        
        d_back = [[False for i in range(ns)] for i in range(ns)]
        dp = [False for i in range(ns+1)]
        dp[0] = True
        


        for i in range(1,1+ns):
            if dp[i-1] == True:
                for j in range(len(wordDict[-1])):
                    if i + j > ns:
                        break
                    if s[i-1:i+j] in wordDict:
                        dp[i+j] = True
                        d_back[i+j-1][max(0,i-1)] = True

        res = [[] for i in range(ns+1)]
        if dp[-1]:
            res = self.back(s, res, d_back, ns)
        else:
            return []
                    
        return res[0]


    def back(self, s, res, d_back, end_id): 
        for i in range(end_id-1,-1,-1):
            if d_back[end_id-1][i] == True:
                if res[end_id] == []:
                    res[i].append(s[i:end_id])
                else:
                    for r in res[end_id]:
                        ts = s[i:end_id]+" "+r
                        if ts not in res[i]:
                            res[i].append(s[i:end_id]+" "+r)

                if i > 0:
                    res = self.back(s, res, d_back, i)

        return res




if __name__ == '__main__':
    s = "pineapplepenapple"; wordDict = ["apple", "pen", "applepen", "pine", "pineapple"]



    solution = Solution()
    print(solution.wordBreak(s, wordDict))


