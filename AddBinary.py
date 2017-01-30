class Solution(object):

    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """

        ai = len(a) - 1
        bi = len(b) - 1
        carry = 0
        sum = ""
        for i in range(max(len(a), len(b))):
            temp = carry
            if ai >= 0:
                temp += int(a[ai])
            if bi >= 0:
                temp += int(b[bi])
            ai -= 1
            bi -= 1
            sum = str(temp % 2) + sum
            carry = temp / 2

        if carry:
            sum = str(carry) + sum
        sum = int(sum)
        return str(sum)

    print addBinary(object, "0", "0")
