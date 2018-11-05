#!/usr/bin/env python


class Solution:
    def maxEnvelopes_n2(self, envelopes):
        """
        :type envelopes: List[List[int]]
        :rtype: int
        """
        N = len(envelopes)
        if N == 0: return 0
        envelopes.sort()    # 按高递增排序
        dp = [1 for i in range(N) if True]  # 排完序后第i个信封可以嵌套的最大层数

        for i in range(1,N):
            for j in range(i,-1,-1):
                if envelopes[j][0] < envelopes[i][0] and envelopes[j][1] < envelopes[i][1]:
                    dp[i] = max(dp[i], dp[j]+1)

        return max(dp)


    def maxEnvelopes(self, envelopes):
        """
        :type envelopes: List[List[int]]
        :rtype: int
        """
        envelopes.sort(key = lambda x: (x[0], -x[1])) # 第一维升序；若第一维相等，第二维降序
        width = [e[1] for e in envelopes if True]
        dp = [0 for i in range(len(envelopes)) if True] # 如果嵌套第i个信封，则最大的信封的最小高度是多少
        length = 0

        import bisect
        for w in width:
            i = bisect.bisect_left(dp, w, 0, length) # 返回将会插入的位置（若重复则左端插入）
            dp[i] = w
            if i == length:
                length += 1

        return length








if __name__ == '__main__':
    envelopes = [[30,50],[12,2],[3,4],[12,15]]

    s = Solution()
    print(s.maxEnvelopes(envelopes))


    # import time
    # start = time.time()
    # print(s.maxEnvelopes_n2(envelopes))
    # dur = time.time() - start
    # print("Time(O(n^2))  : "+str(dur))

    # start = time.time()
    # print(s.maxEnvelopes(envelopes))
    # dur = time.time() - start
    # print("Time(O(nlogn)): "+str(dur))