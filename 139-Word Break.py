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
        if len(wordDict) == 0: return False
        dp = [False for i in range(ns+1)] # dp[i] -- s[0:i]是否可被拆分
        dp[0] = True
        wordDict.sort(key=lambda x:len(x))


        for i in range(ns):
            if dp[i] == True:
                for j in range(1,1+len(wordDict[-1])):
                    if i + j > ns:
                        break
                    if s[i:i+j] in wordDict:
                        dp[i+j] = True

                
        return dp[-1]





if __name__ == '__main__':
    s = "leetcode"; wordDict = ["leet", "code"]

    solution = Solution()
    print(solution.wordBreak(s, wordDict))


