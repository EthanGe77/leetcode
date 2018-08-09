class Solution:
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        carry = 1
        for i in range(len(digits)-1,-1,-1):
            digits[i] += carry
            if digits[i] > 9:
                digits[i] = digits[i] % 10
                carry = 1
            else:
                carry = 0
        if carry == 1:
            digits = [1] + digits
        return digits

a = Solution()
print(a.plusOne([9,9,9]))