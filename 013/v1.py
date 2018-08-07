class Solution:
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        dic = {
            'I' : 1,
            'V' : 5,
            'X' : 10,
            'L' : 50,
            'C' : 100,
            'D' : 500,
            'M' : 1000
        }
        prev_val = 0
        current_val  = 0
        total_sum = 0

        for i in range(len(s)-1,-1,-1):
            if s[i].upper() not in "IVXLCDM":
                raise TypeError("Invalid Input")
            else:
                current_val = dic[s[i]]
                if current_val >= prev_val:
                    total_sum += current_val
                else:
                    total_sum -= current_val
                prev_val = current_val
        return total_sum

a = Solution()
b=a.romanToInt('MCMXCIV')
print(b)