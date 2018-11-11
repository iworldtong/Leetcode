#!/usr/bin/env python

class Solution:
    def candy(self, ratings):
        """
        :type ratings: List[int]
        :rtype: int
        """
        N = len(ratings)
        if N < 2: return N

        s = 1
        f = 1
        r = 0
        for i in range(N-1):
            if ratings[i] < ratings[i+1]:
                if r > 0:
                    f = 2
                    r = 0
                else:
                    f += 1
            elif ratings[i] > ratings[i+1]:
                if r==0:
                    m = f
                r += 1
                f = r
                if r >= m:
                    f += 1      
            else:
                r = 0
                f = 1
            

            s += f

        return s




if __name__ == '__main__':
    test = [1,0,2] # 5
    test = [1,6,10,8,7,3,2] # 18

    s = Solution()
    print(s.candy(test))