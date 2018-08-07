class Solution:
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        ret = ""
        if strs:
        	lenth = min([ len(i) for i in strs])
        else: return ""
        is_equal = True
        for i in range(lenth):
        	test = [x[i] for x in strs]
        	print(test)
        	if len(set(test)) != 1:
        		break
        	else:
        		ret += strs[0][i]
        return ret


a=Solution()
b=a.longestCommonPrefix([""])
print(b)

