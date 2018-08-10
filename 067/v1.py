class Solution:
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        lenth = max(len(a),len(b))
        a = a.zfill(lenth)
        b = b.zfill(lenth)
        carry = 0
        result = ""

        for i in range(lenth-1, -1, -1):
            temp = int(a[i]) + int(b[i]) + carry
            carry = temp // 2
            sum_ = temp % 2
            result += str(sum_)
            # print(f"result {result} carry {carry} sum {sum_}")
        if carry == 1:
            result += "1"
        return result[::-1]


        print(f"{result[::-1]}")

a = Solution()
a.addBinary("101", "1101")