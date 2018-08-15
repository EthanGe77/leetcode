class Solution:
    def arrayPairSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return sum(sorted(nums)[::2])

o = Solution()
r = o.arrayPairSum([1,4,3,2,5,8])
print(r)