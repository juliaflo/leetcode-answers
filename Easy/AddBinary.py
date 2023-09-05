class Solution:
    def addBinary(self, a: str, b: str) -> str:

        if(len(a) > len(b)):
            large = a[::-1]
            small = b[::-1]
        else:
            large = b[::-1]
            small = a[::-1]

        carry = 0
        output = ""
        for i in range(len(large)):
            if i > len(small) - 1:
                total = int(large[i]) + int(carry)
            else:
                total = int(large[i]) + int(small[i]) + int(carry)

            if total == 0:
                output += "0"
            elif total == 1:
                output += "1"
                carry = 0
            elif total == 2:
                output += "0"
                carry = 1
            else:
                output += "1"
                carry = 1

        if carry == 1:
            output += "1"

        return output[::-1]