class Solution:
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        

        max_sum = nums[0]
        cur_sum = nums[0]
        for i in range(1, len(nums)):
            print(nums[i])
            cur_sum = max(nums[i], cur_sum + nums[i])
            max_sum = max(cur_sum, max_sum)
        return max_sum

a = Solution()
print(a.maxSubArray([-2,1]))