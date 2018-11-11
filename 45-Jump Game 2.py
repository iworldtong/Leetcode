#!/usr/bin/env python

class Solution:
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        N = len(nums)
        if N < 2: return 0

        idx = 1
        step = 0
        for i in range(0,N):
            if nums[i] + i >=  N - 1:
                step += 1
                break

            i += idx - 1
            l = [j+nums[i+j] for j in range(1,1+nums[i])]
            print(l)
            m = max(l)
            idx = l.index(m)

            

            step += 1

        return step








if __name__ == '__main__':
    test = [2,3,1,1,4] # 2
    test = [2,0,2,0,1] # 2


    s = Solution()
    print(s.jump(test))




    