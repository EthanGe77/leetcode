class Solution:
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        

        # ret = [i for i in range(1, len(nums)+1) if i not in nums]
        return list(set(range(1,len(nums)+1))-set(nums))

A = Solution()
print(A.findDisappearedNumbers([1,2,2,4,1,5]))
