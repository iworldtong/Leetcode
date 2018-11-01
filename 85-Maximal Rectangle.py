#!/usr/bin/env python

class Solution:
    def maximalRectangle(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        if len(matrix) == 0: return 0

        ROW = matrix.copy()
        CUL = matrix.copy()

        for r,l in enumerate(r):
            for c,i in enumerate(l):
                if r == 0:
                    ROW[r][c] = int(matrix[r][c])
                    if c == 0:
                        CUL[r][c] = int(matrix[r][l])
                    else:




        









if __name__ == '__main__':
    test = [
              ["1","0","1","0","0"],
              ["1","0","1","1","1"],
              ["1","1","1","1","1"],
              ["1","0","0","1","0"]
            ]


    s = Solution()
    print(s.maximalRectangle(test))