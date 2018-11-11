#!/usr/bin/env python

class Solution:
    def numRescueBoats(self, people, limit):
        """
        :type people: List[int]
        :type limit: int
        :rtype: int
        """
        people.sort()



        return people



if __name__ == '__main__':
    people = [1,2]; limit = 3 # 2
    people = [3,2,2,1]; limit = 3 # 3
    people = [3,5,3,4];limit = 5 # 4


    s = Solution()
    print(s.numRescueBoats(people, limit))