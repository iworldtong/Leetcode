#!/usr/bin/env python

class Solution:
    def numRescueBoats(self, people, limit):
        """
        :type people: List[int]
        :type limit: int
        :rtype: int
        """
        N = len(people)
        if N <= 1: return N

        people.sort()

        n = 0
        i = 0
        j = N - 1
        while i <= j:
            if people[i] + people[j] > limit:
                j -= 1
            else:
                j -= 1
                i += 1
            n += 1   
            if i == j:
                n += 1
                break         

        return n



if __name__ == '__main__':
    people = [1,2]; limit = 3 # 2
    people = [3,2,2,1]; limit = 3 # 3
    people = [3,5,3,4];limit = 5 # 4



    s = Solution()
    print(s.numRescueBoats(people, limit))