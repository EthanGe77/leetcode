import math

class Solution:
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        print(math.pow(2,31) -1)
        
        lst = []
        ret = 0
        n = False
        if x < 0:
            x = -x
            n = True
        while x != 0:
            y = x % 10
            ret += y
            ret *= 10
            x = x // 10
            
        ret = ret//10
        if ret >= math.pow(2,31)-1 or x<= -math.pow(2,31):
            return 0
        if n:
            # print(-ret)
            return(-ret)
        else: 
            # print(ret)
            return(ret)