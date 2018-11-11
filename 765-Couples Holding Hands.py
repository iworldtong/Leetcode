#!/usr/bin/env python

class Solution:
    def minSwapsCouples(self, row):
        """
        :type row: List[int]
        :rtype: int
        """
        N = len(row)
        if N <= 2: return 0

        





if __name__ == '__main__':
    row = [0, 2, 1, 3]
    row = [3, 2, 0, 1]


    s = Solution()
    print(s.minSwapsCouples(row))