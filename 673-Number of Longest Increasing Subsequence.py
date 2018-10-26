#!/usr/bin/env python


class Solution:
    def findNumberOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0: return 0

        dp = [[1, 1]]* len(nums) 
        cur_dp = [0, 0]
        for i in range(len(nums)):
            for j in range(0, i):
                if nums[i] > nums[j]:
                    if dp[i][0] == dp[j][0]+1:
                        dp[i][1] += dp[j][1]
                    elif dp[i][0] < dp[j][0]+1:
                        dp[i] = [dp[j][0]+1, dp[j][1]]
            if dp[i][0] > cur_dp[0]:
                cur_dp = [dp[i][0], dp[i][1]]
            elif dp[i][0] == cur_dp[0]:
                cur_dp[1] += dp[i][1]
        
        return cur_dp[1]
        



if __name__ == '__main__':
    test = [1,1,1,2,2,2,3,3,3]

    s = Solution()
    print(s.findNumberOfLIS(test))
