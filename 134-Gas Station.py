#!/usr/bin/env python

class Solution:
    def canCompleteCircuit(self, gas, cost):
        """
        :type gas: List[int]
        :type cost: List[int]
        :rtype: int
        """
        N = len(gas)
        delta = [gas[i] - cost[i] for i in range(N)]
        if sum(delta) < 0: return -1

        s = 0
        tmp_sum = -delta[0]
        tmp = -1
        for i in range(N):
            tmp_sum += delta[i]
            if delta[i] >= 0 and tmp == -1:
                tmp = i
                tmp_sum = delta[i]
            elif delta[i] < 0 and tmp == -1:
                s += delta[i]
            elif tmp_sum < 0:
                s += tmp_sum
                tmp = -1

        return tmp





if __name__ == '__main__':
    gas  = [1,2,3,4,5]; cost = [3,4,5,1,2] # 3
    gas = [6,1,4,3,5]; cost = [3,8,2,4,2] # 2
    gas = [7,1,0,11,4]; cost = [5,9,1,2,5] # 3


    s = Solution()
    print(s.canCompleteCircuit(gas, cost))


