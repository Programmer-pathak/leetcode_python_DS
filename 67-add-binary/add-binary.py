class Solution:
    def addBinary(self, a: str, b: str) -> str:
        #return bin(int(a, 2) + int(b, 2))[2:]

        res = []
        carry = 0
        i, j = len(a) - 1, len(b) - 1

        # Traverse both strings from right to left
        while i >= 0 or j >= 0 or carry:
            total = carry
            
            if i >= 0:
                total += int(a[i])
                i -= 1
            if j >= 0:
                total += int(b[j])
                j -= 1
            
            # Append remainder (0 or 1) to result
            res.append(str(total % 2))
            # Calculate new carry (0 or 1)
            carry = total // 2
        
        # Reverse the array and join into string
        return "".join(res[::-1])