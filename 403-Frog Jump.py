
class Solution:
    def canCross(self, stones):
        """
        :type stones: List[int]
        :rtype: bool
        """

        dp = {stone: {} for stone in stones}
        dp[0][0] = 0
        for stone in stones:
            for step in dp[stone].values():
                for k in [step + 1, step, step - 1]:
                    if k > 0 and stone + k in dp: # do not use stones -- time out
                        dp[stone + k][stone] = k
        return len(dp[stones[-1]].keys()) > 0

        

if __name__ == '__main__':

    test = [0,1,3,4,5,7,9,10,12]
    s = Solution()

    print(s.canCross(test))







