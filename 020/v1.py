class Solution:
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        lenth = len(s)
        while True :
        	lenth = len(s)
        	s = s.replace("{}","")
        	s = s.replace("[]","")
        	s = s.replace("()","")
        	if lenth == len(s):
        		break;
        if len(s) != 0:
        	return False
        else: return True

# Not a very elegant solution
a = Solution()
print(a.isValid("{}[]{}(a)"))
