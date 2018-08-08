class Solution:
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums: return 0
        end = 0
        for i in range(1,len(nums)):
            if nums[end] != nums[i]:
                end += 1
                nums[end] = nums[i]
        return end + 1





a = Solution()
print(a.removeDuplicates([1,2,2,2,2,2,3,3,4,5,6,7]))

