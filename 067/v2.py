class Solution:
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        c = str(int(a) + int(b))
        carry = '0'
        result = ""

        for i in range(len(c)-1, -1, -1):
            if c[i] == '0':
                    result += carry
                    carry = '0'

            elif c[i] == '1':
                if carry == '0':
                    result += '1'
                    carry = '0'
                else:
                    result += '0'
                    carry = '1'
            else:
                result += carry
                carry = '1'
        if carry == '1':
            result += '1'
            # print(f"result {result} carry {carry} sum {sum_}")
        # return result[::-1]


        print(f"{result[::-1]}")

a = Solution()
a.addBinary("111", "111")