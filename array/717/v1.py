class Solution:
    def isOneBitCharacter(self, bits):
        """
        :type bits: List[int]
        :rtype: bool
        """
        lenth = len(bits)
        if lenth==1: return True
        i = 0
        while i < lenth:
        	print(f"i is {i} bits[i] is {bits[i]}")
        	if i == lenth - 1 and bits[i] == 0:
        		return True
        	elif i == lenth - 2 and bits[i] == 1:
        		return False
        	if bits[i] == 1:
        		i += 2
        	elif bits[i] == 0:
        		i += 1


a = Solution()
print(a.isOneBitCharacter([0, 0]))