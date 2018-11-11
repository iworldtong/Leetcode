#!/usr/bin/env python

class Solution:
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        N = len(nums)
        if N == 0: return False
        if N == 1: return True
        elif nums[0] == 0: return False

        for i in range(1,N):
            if nums[i] == 0:
                for j in range(i-1,-1,-1):
                    print(str(i)+' '+str(j))
                    if nums[j] > (i - j):
                        break
                    if i == N - 1 and nums[j] > (i - j - 1):
                        return True
                    if j == 0:
                        return False
            

        return True








if __name__ == '__main__':
    test = [4,2,0,0,1,1,4,4,4,0,4,0] # True
    test = [2,0,0,0]


    s = Solution()
    print(s.canJump(test))




    