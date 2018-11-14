#!/usr/bin/env python

class Solution:
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        N = len(nums)
        if N < 2: return 0

        idx = 0
        step = 0
        for i in range(0,N):
            i = idx
            if nums[i] + i >=  N - 1:
                step += 1
                break
            m = 0
            for j in range(1,1+nums[i]):
                if nums[i+j] > 0:
                    if j + nums[i+j] > m:
                        idx = i + j
                        m = j + nums[i+j]

            step += 1

        return step








if __name__ == '__main__':
    test = [2,3,1,1,4] # 2
    test = [2,0,2,0,1] # 2
    test = [2,0,2,4,6,0,0,3]

    s = Solution()
    print(s.jump(test))




    