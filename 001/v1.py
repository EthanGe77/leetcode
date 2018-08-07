class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        i, j = 0, 1

        while i < len(nums):

        	while j < len(nums):
        		if nums[i] + nums[j] == target:
        			return [i, j]
        		j += 1
        	i += 1
        	j = i+1
        return []


a = Solution()
print(a.twoSum([2, 7, 11, 15], 22))
