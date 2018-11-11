#!/usr/bin/env python

class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        N = len(prices)

        p = 0
        max_profit = 0
        tmp = 0
        while True:
            if p >= N - 1: 
                break

            for i in range(p+1, N):
                cur = prices[i] - prices[p]
                if cur > tmp:
                    if i == N - 1:
                        max_profit += cur
                        p = i
                    else:
                        tmp = cur
                else:
                    p = i
                    max_profit += tmp
                    tmp = 0
                    break

        return max_profit



if __name__ == '__main__':
    test = [7,1,5,3,6,4] # 7
    # test = [1,2,3,4,5] # 4


    s = Solution()
    print(s.maxProfit(test))