#!/usr/bin/env python

class Solution:
    def countBits(self, num):
        """
        :type num: int
        :rtype: List[int]
        """
        dp = [0 for i in range(num+1) if True]
        

        even = False
        for i in range(1, num + 1):
            if even:
                dp[i] = dp[i // 2] # 十进制乘2相当于对应二进制左移1位，对应“1”的个数不变
            else:
                dp[i] = dp[i-1] + 1 

            even = True if even == False else False            

        return dp





if __name__ == '__main__':
    test = 16 # [0,1,1,2,1,2,2,3,1,2,2,3,2,3,3,4,1]

    s = Solution()
    print(s.countBits(test))