class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        check={}
        for i, num in enumerate(nums):
            test = check.get(num)
            if test == None:
                check[target - num] = i
            else:
                return [test, i]




a = Solution()
print(a.twoSum([2, 7, 11, 15], 26))







 # [2, 7, 11, 15], target = 9,