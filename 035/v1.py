class Solution:
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        ret = len([num for num in nums if target > num])
        return ret


a = Solution()

print(a.searchInsert([1,3,5,6],0))
