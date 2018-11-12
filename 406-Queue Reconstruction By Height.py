#!/usr/bin/env python
import time
class Solution:
    def reconstructQueue(self, people):
        """
        :type people: List[List[int]]
        :rtype: List[List[int]]
        """
        N = len(people)
        if N < 2: return people

        people.sort(key=lambda x: [x[0], -x[1]])

        r_people = [people[-1]]
        for i in range(N-2, -1, -1):
            r_people.insert(people[i][1],people[i])                

        return r_people


if __name__ == '__main__':
    people = [[7,0], [4,4], [7,1], [5,0], [6,1], [5,2]]

    s = Solution()
    print(s.reconstructQueue(people))