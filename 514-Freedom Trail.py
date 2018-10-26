class Solution:
    def findRotateSteps(self, ring, key):
        """
        :type ring: str
        :type key: str
        :rtype: int
        """
        steps = 0
        for k in key:
            self.match(ring, k)



    def match(self, l, s):
        return [l_ring.index(s,i) for i in range(l.count(s)) if True]
            

        




if __name__ == '__main__':
    ring = "godding"
    key = "gd" # 4


    s = Solution()
    print(s.findRotateSteps())