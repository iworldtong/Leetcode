class Solution:
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        left = 0
        right = len(nums)-1
        max_sum = self.divide(nums, left, right)        

        return max_sum

    def divide(self, nums, left, right):
        if left == right:
            return nums[left]
        center = (left + right) // 2
        l_max_sum = self.divide(nums, left, center)
        r_max_sum = self.divide(nums, center + 1, right)

        lb_sum = nums[center]
        l_sum = nums[center]
        for i in range(center-1, left-1, -1):
            l_sum += nums[i]
            if l_sum > lb_sum:
                lb_sum = l_sum

        rb_sum = nums[center+1]
        r_sum = nums[center+1]
        for i in range(center+2, right+1):
            r_sum += nums[i]
            if r_sum > rb_sum:
                rb_sum = r_sum
        
        m_max_sum = lb_sum + rb_sum

        return max(l_max_sum, r_max_sum, m_max_sum)