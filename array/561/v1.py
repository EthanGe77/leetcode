class Solution:
    def arrayPairSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        sum = 0
        for i in range(len(nums)//2):
        	sum += min(nums[2*i],nums[2*i + 1])
        	print(sum)
        return sum

o = Solution()
r = o.arrayPairSum([1,4,3,2,5,8])
print(r)