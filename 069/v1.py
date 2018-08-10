class Solution:
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x == 1:
        	return 1
        left = 0
        right = x
        mid = x/2
        diff = abs(mid*mid - x)

        while diff > 0.000001:
        	if mid * mid > x:
        		right = mid
        	else:
        		left = mid
        	mid = (left + right)/2
        	diff = abs(mid*mid - x)
        return int(mid)


a=Solution()
print(a.mySqrt(4))

