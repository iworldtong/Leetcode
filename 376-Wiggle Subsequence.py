#!/usr/bin/env python

class Solution:
    def wiggleMaxLength(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        N = len(nums)
        if N < 2: return N

        n = nums[0]
        pos = None
        cnt = 1
        for i in range(1,N):
            if nums[i-1] != nums[i]:
                if pos is None:
                    pos = nums[i] > nums[i-1]
                    n = nums[i]
                    cnt += 1
                elif pos:
                    if nums[i] < n:
                        cnt += 1
                        pos = False
                    n = nums[i]
                else:
                    if nums[i] > n:
                        cnt += 1
                        pos = True
                    n = nums[i]

        return cnt





if __name__ == '__main__':
    nums = [1,7,4,9,2,5]

    s =Solution()
    print(s.wiggleMaxLength(nums))