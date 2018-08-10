class Solution:
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x <=1:
            return x

        for i in range (1,x+1):
            if i * i > x:
                return int(i - 1)
            elif i * i == x:
                return int(i)
            else:
                continue


a=Solution()
print(a.mySqrt(2))

