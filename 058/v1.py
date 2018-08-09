class Solution:
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        if s:
        	lst = s.split()
        else: return 0
        if lst:
        	return len(lst[-1])
        else: return 0
        # return 

a = Solution()
a.lengthOfLastWord(" ")